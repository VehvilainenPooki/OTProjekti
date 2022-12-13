class Camera:


    def __init__(self, game_player, reso):
        self.cam_player = game_player
        self.p_radius = self.cam_player.get_hitbox_r()
        pos = game_player.get_pos()
        self.resolution = reso
        self.posx = pos[0]
        self.posy = pos[1]

    def get_pos(self):
        p_pos = self.cam_player.get_pos()
        self.posx = p_pos[0] - (self.resolution[0]/2-self.p_radius)
        self.posy = p_pos[1] - (self.resolution[1]/2-self.p_radius)
        return (self.posx, self.posy)
