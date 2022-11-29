```mermaid
 classDiagram
      class Player{
          location
          health
          weapons
          weaponInUse
          get_location()
          attack()
          get_health()
      }
      class Move{
          update_player_pos()
      }
      class Camera{
          move_camera()
      }
      class Monster{
          health
      }
      class World{
          import_world_chunk()
      }
      class Sprite{
          position
          image
      }
      class Resource{
          type
          purity
          toughness
          mine_resource()
      }
      class Thegame{
          start()
          update()
      }
      Thegame ..> Player
      Thegame ..> Move
      Thegame ..> Monster
      Thegame ..> World
      Move ..> Player
      World ..> Sprite
      World ..> Resource
```mermaid
