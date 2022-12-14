## The architecture diagram of the game.
```mermaid
 classDiagram
      class Player{
          position
          health
          hitbox
          take_damage()
          get_health()
      }
      class Movement{
          move()
      }
      class Chunkloader{
          initialize_level()
          load_zone()
          get_player()
          get_pointer()
      }
      class TerrainSprite{
          position
          hitbox
          image
      }
      class GameloopHandler{
          resolution
          scale
          start_loop()
      }
      class Adventure{
          gameloop()
      }
      class Menu{
          mainmenu_screen()
          settingsmenu_screen()
      }
      class Collisions{
          are_colliding()
          remove_collision()
      }
      GameloopHandler ..> Menu
      GameloopHandler ..> Adventure
      Adventure ..> Player
      Adventure ..> Movement
      Adventure ..> Chunkloader
      Movement ..> Player
      Chunkloader ..> TerrainSprite
      Chunkloader ..> Player
      Adventure ..> Collisions
      Collisions ..> Player
      Collisions ..> TerrainSprite
```

## Example logic sequence diagram: Player collision with terrainsprite
On every frame the game checks if the player is colliding with anything are_colliding(player, sprite). If there is a collision then the Adventure class chooses what to do. In this case it runs the method remove_collision(player, sprite) which separates the player and the sprite. are_colliding() and remove_collision() both check if there is a collision. are_colliding() returns this info as a boolean statement. remove_collision() then calculates the minimum distance to move the sprite to separate them and moves the first arguments sprite.
```mermaid
sequenceDiagram
  participant Adventure
  participant Collisions
  actor Player
  participant TerrainSprite
  Adventure->>+Collisions: are_colliding(player, sprite)
  Collisions->>Player: .rect.center
  Player-->>Collisions: tuple(pos)
  Collisions->>Terrainsprite: .rect.center
  Terrainsprite-->>Collisions: tuple(pos)
  Collisions-->>-Adventure: True
  Adventure->>+Collisions: remove_collision(player, sprite)
  Collisions->>Player: .rect.center
  Player-->>Collisions: tuple(pos)
  Collisions->>Terrainsprite: .rect.center
  Terrainsprite-->>Collisions: tuple(pos)
  Collisions->>-Player: set_pos(x,y)
```

