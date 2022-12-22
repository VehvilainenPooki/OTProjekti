


class Renderer():
    def __init__(self) -> None:
        pass

    def render_frame(self, screen, sprites, cam):
        #screen.blit(self.background, (0, 0))
        cam_offset = cam.get_pos()
        for sprite in sprites:
            s_pos = sprite.get_rendering_pos()
            screen.blit(sprite.image, (s_pos[0] -
                        cam_offset[0], s_pos[1]-cam_offset[1]))