import math

class Collisions:

    def __init__(self, game_player):
        self.player = game_player
        self.p_radius = self.player.get_hitbox_r()

    def are_colliding(self, circle):
        dist_p_c = math.dist(self.player.rect.center, circle.rect.center)
        c_radius = circle.get_hitbox_r()
        if self.p_radius+c_radius > dist_p_c:
            return True
        return False
