class ImageState:
    def __init__(self, day_image, night_image):
        self.day_image = day_image
        self.night_image = night_image

        self.current = self.day_image

    def get_state(self, code):
        match code:
            case "day":
                self.current = self.day_image
            case "night":
                self.current = self.night_image
                

# class Sprite:
#     def __init__(self, width: int, height: int, color: tuple[int, int, int], transparent: bool, **kwargs):
#         self.surface = pg.Surface((width, height))
#         if transparent:
#             self.surface = pg.Surface((width, height), 32, pg.SRCALPHA)

#         self.surface.fill(color)
        
#         self.rect = self.surface.get_rect(**kwargs)
    
#     def draw_self(self):
#         ds.screen.blit(self.surface, self.rect)
    
#     def get_image(self, image: pg.Surface):
#         self.surface.blit(image)

# class ImageAnimation:
#     def __init__(self, images: tuple, speed: float, **kwargs):
#         self.images = images
#         self.index = 0
#         self.speed = speed  # 0 -> 1 high speed == fast animation

#         self.surf = self.images[self.index]
#         self.rect = self.surf.get_rect(**kwargs)

#     def toggle_animation(self):
#         self.index += self.speed
#         if self.index >= len(self.images):
#             self.index = 0

        # self.surf = self.images[int(self.index)]
        # ds.screen.blit(self.surf, self.rect)