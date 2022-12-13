import math

class Collisions:
    """Handles everything related to collisions. 

    """


    def __init__(self, game_player):
        self.player = game_player
        self.p_radius = self.player.get_hitbox_r()

    def are_colliding(self, circle):
        dist_p_c = math.dist(self.player.rect.center, circle.rect.center)
        c_radius = circle.get_hitbox_r()
        if self.p_radius+c_radius > dist_p_c:
            return True
        return False

    def remove_collision(self, circle):
        #Checking how much to move the player
        p_pos = self.player.rect.center
        c_pos = circle.rect.center
        dist_p_c = math.dist(p_pos, c_pos)
        c_radius = circle.get_hitbox_r()
        p_c_overlap = (self.player.get_hitbox_r()+c_radius)-dist_p_c

        if p_c_overlap < 0:
            return

        dist_x = math.dist([p_pos[0]], [c_pos[0]])
        dist_y = math.dist([p_pos[1]], [c_pos[1]])
        if dist_p_c == 0:
            self.player.add_pos(1, 1)
            return
        dist_x = math.ceil(dist_x*(p_c_overlap/dist_p_c))
        dist_y = math.ceil(dist_y*(p_c_overlap/dist_p_c))
        #Checking which direction to move the player
        if p_pos[0] < c_pos[0]:
            dist_x = -dist_x
        if p_pos[1] < c_pos[1]:
            dist_y = -dist_y

        #Moving the player
        self.player.add_pos(dist_x, dist_y)
