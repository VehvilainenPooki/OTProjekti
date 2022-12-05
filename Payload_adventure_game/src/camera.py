from player import Player

class Camera:
    WIDTH = 800
    HEIGHT = 400


    def __init__(self, p):
        self.cam_player = p
        self.r = self.cam_player.get_hitbox_r()
        pos = p.get_pos()
        self.posx = pos[0]
        self.posy = pos[1]
    
    def get_x(self):
        a = self.cam_player.get_pos()
        self.posx = a[0] - (self.WIDTH/2-self.r)
        return self.posx

    def get_y(self):
        a = self.cam_player.get_pos()
        self.posy = a[1] - (self.HEIGHT/2-self.r)
        return self.posy
    