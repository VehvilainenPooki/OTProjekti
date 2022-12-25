import pygame


class Renderer():
    """Renderer class renders frames from selected cameras perspective.
    """

    def __init__(self, resolution, scale, camera):
        """Renderer class constructor

        Args:
            resolution (tuple): window resolution
            scale (int): scaling value
            camera (Camera): The camera that gives the renderers perspective
        """
        self.resolution = resolution
        self.scale = scale
        self.cam = camera

    def render_frame(self, screen, sprites):
        """Draws sprites to screen from self.cam perspective.

        Args:
            screen (pygame.display): The window of the game.
            sprites (pygame.sprite.Group): Sprite group to be drawn.
        """
        background = pygame.Surface((3840, 2160))
        background.fill((50, 100, 50))
        screen.blit(background, (0, 0))
        cam_offset = self.cam.get_pos()
        for sprite in sprites:
            s_pos = sprite.get_pos()
            size = sprite.image.get_size()
            screen.blit(pygame.transform.scale(sprite.image, (size[0]*self.scale, size[1]*self.scale)), (s_pos[0] - (cam_offset[0]+size[0]/2)*self.scale,
                                                                                                         s_pos[1]-(cam_offset[1]+size[1]/2)*self.scale))

    def set_camera(self, camera):
        """Sets the camera that the renderer uses

        Args:
            camera (Camera): The camera object that tells the renderer the perspective.
        """
        self.cam = camera

    def update_scaling(self, resolution, scale):
        """Updates the scaling that the renderer uses

        Args:
            resolution (tuple): current resolution of the screen
            scale (int): current scaling multiplier
        """
        self.resolution = resolution
        self.scale = scale/10
