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
      class SimpleMob{
          position
          hitbox
          health
          damage()
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
      GameloopHandler ..> Menu
      GameloopHandler ..> Adventure
      Adventure ..> Player
      Adventure ..> Movement
      Adventure ..> SimpleMob
      Adventure ..> Chunkloader
      Movement ..> Player
      Chunkloader ..> TerrainSprite
      Chunkloader ..> Player
```

## Example logic sequence diagram: Player collision with terrainsprite
On every frame the game checks if the player is colliding with anything. If there is a collision then the game chooses what to do. In this case it runs the method remove_collision(terrainsprite) which moves the player so it just touches it. are_colliding() and remove_collision() both check that there is a collision. are_colliding() reports this by returning True if they are colliding. remove_collision() then calculates the minimum distance to move the object to separate them.
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

