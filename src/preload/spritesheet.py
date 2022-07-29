import os
import json
import pygame as pg

class Spritesheet:
    def __init__(self, image_path: str, config_path: str | None = None, meta_data_path: str | None = None):
        head, _ = os.path.split(image_path)

        actual_config_path = f'{head}/config.json' if config_path is None else config_path
        actual_meta_data_path = f'{head}/hash.json' if config_path is None else meta_data_path
        
        with (
            open(actual_config_path, 'r') as config,
            open(actual_meta_data_path, 'r') as meta
        ):
            self.config = json.load(config)
            self.meta_data = json.load(meta)

        if self.config['transparent']:
            self.sprite_sheet = pg.image.load(image_path).convert_alpha()
            return

        self.sprite_sheet = pg.image.load(image_path).convert()


    def get_sprite(self, x: int, y: int, width: int, height: int) -> pg.Surface:
        """
        (not recommended)
        get sprite directly from the spritesheet using x, y coordinates and width, height of the image
        """
        sprite = pg.Surface((width, height), pg.SRCALPHA, 32)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return sprite

    def parse_sprite(self, name: str, angle: float | None = None, scale: float | None = None) -> pg.Surface:
        """
        (recommended)
        get sprite from the spritesheet using the name of the sprite in the metadata
        """
        sprite = self.meta_data['frames'][name]['frame']
        x, y, width, height = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        angle = angle if angle is not None else self.config['angle']
        scale = scale if scale is not None else self.config['scale']

        image = pg.transform.rotozoom(self.get_sprite(x, y, width, height), angle, scale)

        return image