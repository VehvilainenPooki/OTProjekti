class Camera:
    """Class that handles moving the view so that the player is in the middle.
    """

    def __init__(self, follow_entity):
        """Classes constructor which creates a camera that tracks a sprite

        Args:
            follow_entity (Player): The entity that the camera will track
        """
        self.cam_entity = follow_entity
        self.sprite_radius = self.cam_entity.get_hitbox_r()

    def get_pos(self):
        """Returns the current location of the camera object

        Returns:
            tuple: Coordinates of the camera as an tuple (x, y)
        """
        p_pos = self.cam_entity.get_pos()
        posx = p_pos[0] - (960-self.sprite_radius)
        posy = p_pos[1] - (540-self.sprite_radius)
        return (posx, posy)
