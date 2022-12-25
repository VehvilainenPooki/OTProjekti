import math


class Collisions:
    """Handles everything related to collisions.

    """

    def __init__(self, game_player):
        """Classes constructor which creates the collision handler

        Args:
            game_player (Player): The games player object
        """
        self.player = game_player
        self.p_radius = self.player.get_hitbox_r()

    def are_colliding(self, circle1, circle2):
        """Checks if two entities are colliding. Uses circle collision.

        Args:
            circle1 (Sprite): The sprite of an entity
            circle2 (Sprite): The sprite of an entity

        Returns:
            bool: Returns True if the entities are colliding
        """
        dist_p_c = math.dist(circle1.rect.center, circle2.rect.center)
        c_radius = circle2.get_hitbox_r()
        if self.p_radius+c_radius > dist_p_c:
            return True
        return False

    def remove_collision(self, moving, static):
        """Removes the collision of two entities.
            The method will only move the moving args sprite.

        Args:
            circle (Sprite): The sprite of an entity
        """
        p_pos = moving.rect.center
        c_pos = static.rect.center
        dist_p_c = math.dist(p_pos, c_pos)
        c_radius = static.get_hitbox_r()
        p_c_overlap = (moving.get_hitbox_r()+c_radius)-dist_p_c

        if p_c_overlap < 0:
            return

        dist_x = math.dist([p_pos[0]], [c_pos[0]])
        dist_y = math.dist([p_pos[1]], [c_pos[1]])

        if dist_p_c == 0:
            moving.add_pos(1, 1)
            return

        dist_x = math.ceil(dist_x*(p_c_overlap/dist_p_c))
        dist_y = math.ceil(dist_y*(p_c_overlap/dist_p_c))

        if p_pos[0] < c_pos[0]:
            dist_x = -dist_x
        if p_pos[1] < c_pos[1]:
            dist_y = -dist_y

        moving.add_pos(dist_x, dist_y)
