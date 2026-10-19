#include "dm.h"
#include <signal.h>

extern void dm_gate(void);
static pthread_key_t allocation_key;
static pthread_once_t allocation_once = PTHREAD_ONCE_INIT;
void crash_thread_init(void);
static void free_state(void *pointer) {
    void **state = pointer;
    free(state[0]);
    free(state[1]);
    free(state);
}
static void create_key(void) {
    if (pthread_key_create(&allocation_key, free_state)) die("Cannot create guest state key");
}
void guest_thread_init(void) {
    crash_thread_init();
    pthread_once(&allocation_once, create_key);
    if (pthread_getspecific(allocation_key)) return;
    void **state = calloc(2, sizeof(void *));
    if (!state) die("Cannot allocate guest thread state");
    state[0] = calloc(1, 8192);
    uint8_t *region = calloc(1, 0x600);
    state[1] = region;
    if (!state[0] || !state[1]) die("Cannot allocate guest TLS");
    *(void **)(region + 0x1f8) = region + 0x200;
    if (pthread_setspecific(allocation_key, state) ||
        pthread_setspecific(g_key18, NULL) ||
        pthread_setspecific(g_keygate, (void *)dm_gate) ||
        pthread_setspecific(g_keytls, state[0]) ||
        pthread_setspecific(g_keytlr, region)) die("Cannot initialize guest thread slots");
}
