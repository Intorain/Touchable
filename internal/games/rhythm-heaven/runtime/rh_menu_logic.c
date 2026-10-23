#include "rh_menu_logic.h"
#include <math.h>

float rh_menu_scroll_limit(float value, int count, int slots, int low, int high, float spacing) {
    if (!isfinite(value) || !isfinite(spacing) || spacing <= 0 || count <= 0 || slots <= 0) return 0;
    float minimum = (-low - slots / 2) * spacing;
    float maximum = (count - 1 - high - slots / 2) * spacing;
    return fminf(fmaxf(value, minimum), fmaxf(minimum, maximum));
}
