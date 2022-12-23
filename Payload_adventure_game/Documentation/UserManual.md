# UserManual
## Install
1. Download the newest release from [here](https://github.com/VehvilainenPooki/OTProjekti/releases/)
2. Unzip the folder into a place you like
3. Open a terminal window in ../OTProjekti/Payload_adventure_game/ folder
4. Install dependencies with:
```bash
poetry install
```
5. Start the game with:
```bash
poetry run invoke start
```
If you are using windows this won't most likely work. This is because of pty.

For Windows run:
```bash
poetry run python .\src\index.py
```
## Menu
The menu is navigated with the mouse. Just hover over the button you want to interact with and click the mouse1 button of your mouse.
### Mainmenu
- [Start]: Starts the game
- [Settings]: Opens the settings menu
- [Quit]: Exits the game
### Settingsmenu
- [Resolution]: cycles through the resolution options
- [Apply]: Changes the window to the selected resolution
- [Back]: Goes back to the mainmenu
## Game
### Controls
At this point in time the game has these controls:
- [WASD]: Moves the player around.
- [SHIFT]: Makes the player sprint. (move faster)
- [CTRL]: Makes the player sneak. (move slower)
- [SPACE]: Makes the player do a short dash in the current movement direction. This has a 30 frame cooldown.
- [Mouse_position]: Aiming.
- [ESC]: Closes the game.
