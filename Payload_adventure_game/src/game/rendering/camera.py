class Camera:
    """Class that handles moving the view so that the player is in the middle.
    """

    def __init__(self, game_player, reso, scale):
        """Classes constructor which creates the Camera

        Args:
            game_player (Player): The player object of the game
            reso (tuple): The resolution of the screen
        """
        self.cam_player = game_player
        self.p_radius = self.cam_player.get_hitbox_r()
        pos = game_player.get_pos()
        self.resolution = reso
        self.posx = pos[0]
        self.posy = pos[1]
        self.scale = scale

    def get_pos(self):
        """Returns the current location of the camera object

        Returns:
            tuple: Coordinates of the camera as an tuple (x, y)
        """
        p_pos = self.cam_player.get_pos()
        self.posx = p_pos[0] - (self.resolution[0]/2-self.p_radius)
        self.posy = p_pos[1] - (self.resolution[1]/2-self.p_radius)
        return (self.posx, self.posy)

    def update_scaling(self, reso, scale):
        self.resolution = reso
        self.scale = scale