import pygame as pg
import src.preload.assets as assets
from src.comp.export.sub_process import Process


class LostScreen(Process):
    def __init__(self, game):
        super().__init__(game, 'G A M E  O V E R', assets.Gallery.RETRY_BUTTON)

    def on_click_event(self):
        self.reset_game()

    def reset_game(self):
        self.game.time_state = self.game.config["timeState"]
        self.game.modifier.reset()
        self.game.global_flag.reset()
        # self.game.dino.reset()
        self.game.background.reset()
        self.game.score_system.reset()
        self.game.obstacle_manager.reset()
        self.game.paused_screen.change_state()
        self.change_state()
