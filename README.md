###### This is an WIP project that is being developed for a course from the University of Helsinki https://ohjelmistotekniikka-hy.github.io/
# Payload_adventure_game
### Game with a take on the classic payload mission. Travel a world while protecting your waggon, collecting resource, and unlocking new abilities.
## About Python version
### This project is being developed in python 3.8.10. It might have issues if ran with an older version of python.
## Documentation
### [Vaatimusmäärittely](https://github.com/VehvilainenPooki/OTProjekti/blob/main/Payload_adventure_game/Documentation/Payload_adventure_game.md) (Requirements specification)
### [ArchitectureDescription](https://github.com/VehvilainenPooki/OTProjekti/blob/main/Payload_adventure_game/Documentation/ArchitectureDescription.md)
### Testing documents (WIP)
### [Working Hours Log](https://github.com/VehvilainenPooki/OTProjekti/blob/main/Payload_adventure_game/Documentation/WorkingHoursLog.md)
### [ChangeLog](https://github.com/VehvilainenPooki/OTProjekti/blob/main/Payload_adventure_game/Documentation/ChangeLog.md)
### [Release](https://github.com/VehvilainenPooki/OTProjekti/releases/tag/viikko5)
## Install
1. Install dependencies with:
```bash
poetry install
```
2. Start the game with:
```bash
poetry run invoke start
```
## Commandline functionality
Start the game:
```bash
poetry run invoke start
```
Test the code:
```bash
poetry run invoke test
```
Run coverage-report:
```bash
poetry run invoke coverage-report
```
Run Pylint code analysis:
```bash
poetry run invoke lint
```
Auto format to PEP8:
```bash
poetry run invoke format
```
