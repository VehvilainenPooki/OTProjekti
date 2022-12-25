# TestingDocument
## UnitTesting
### UI
UI elements are not included in testing. `Rendering` and `Camera`.
### Gameloop
Gameloop classes have quite little testing. They aren't really written to be tested. I learned step by step and didn't have the time to fix the classes: 
`GameloopHandler`, `Menu` and `Adventure`.
### Logic
`Collisions` and `Movement` are tested most thoroughly with `Movement` only missing the tests that have player input in the method.
### World
`Chunkloader` has good test for functional use but there is no test for incorrect inputs and exceptions.
### Entities
`Player` and `TerrainSprite` have quite a bit of testing through the `Movement` and`Collisions` tests. However the `Pointer` class has quite poor tests
and the whole class should be rewritten.

##Test coverage
(UI is excluded from the table.)
![http://url/to/img.png](https://raw.githubusercontent.com/VehvilainenPooki/OTProjekti/main/Payload_adventure_game/Documentation/Images/coverage_table.png)

Testing remained minimal in the through out of this course. This was mostly because of prioritization and exitement of new features
and my poor understanding of multi file programming practices and coding for tests.
## SystemTesting
The system was tested manually.
### Install and configuration
The game has been downloaded and setup following the
[User manuals](https://github.com/VehvilainenPooki/OTProjekti/blob/main/Payload_adventure_game/Documentation/UserManual.md)
steps with multiple devices, operating systems (windows, linux) and environments.
The game has been tested with and without the config file. To Force the game to create the config file.
### Features
All completed points from the [requirements_specififation](https://github.com/VehvilainenPooki/OTProjekti/blob/main/Payload_adventure_game/Documentation/UserManual.md)
have been throughly tested with multiple inputs in "correct" and "incorrect" ways.
# Remaining bugs and missing qualities
The Adventure gameloop has major problems with scaling especially while moving.
Chunkloader doesn't handle any exceptions and is easily broken.
Testing is insufficient in unittesting and integrationtesting.
The classes need more seperation with UI and logic.
Dependency injection needs work especially with `menu` and `GameloopHandler`.
