# Installation packages

After a build completes, find the `.ipa` in the applicable game folder.
The `.json` file with the same name records the game identity, the signature expiry date, and the SHA-256.
Use the `.sha256` file with the same name to verify the file.

1. Double-click `Touchable.command` at the top level.
2. Select a game.
3. Select "Install existing IPA".

After a new IPA passes the checks, the old IPA moves into a hidden local archive.
This process does not delete old files.
Each game keeps its own current IPA.
The package contains local game assets. Do not commit it to Git.
