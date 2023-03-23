import sys
import pygame as pg
from src.preload.settings import *
from pygame.locals import QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, WINDOWFOCUSLOST, WINDOWMOVED

class Game:
    def __init__(self):
        pg.mixer.pre_init(44100, -16, 2, 512)
        pg.init()

        pg.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, WINDOWFOCUSLOST, WINDOWMOVED])
        pg.display.set_caption("Python Dinosaur")

        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

        ICON = pg.image.load('./assets/img/icon/dino.ico').convert_alpha()
        pg.display.set_icon(ICON)

        self.new_game()

    def new_game(self):
        # from src.comp.other.dino import Dino
        from src.preload.config_reader import config
        from src.comp.other.score_sys import ScoreSys
        from src.comp.other.background import Background
        from src.comp.other.lost_screen import LostScreen
        from src.comp.other.obstacle import ObstacleManager
        from src.comp.other.paused_screen import PausedScreen
        from src.comp.other.modifier import Modifier, GlobalFlag

        # Config
        self.config = config
        self.modifier = Modifier(self)
        self.global_flag = GlobalFlag(self)

        # General game's attributes
        self.time_state = config["timeState"]

        # UI & Objects
        self.paused_screen = PausedScreen(self)
        self.lost_screen = LostScreen(self)
        self.background = Background(self)
        self.score_system = ScoreSys(self)
        self.obstacle_manager = ObstacleManager(self)
        # self.dino = Dino(self)

    def draw(self):
        self.background.update()

    def update(self):
        """
        For updating and drawing main components
        """
        self.delta_time = float(self.clock.tick(FPS)/1000)

        if self.global_flag.trigger_main_game:
            self.obstacle_manager.update()
        self.score_system.update()

        if self.paused_screen.run:
            self.paused_screen.activate()
        elif self.lost_screen.run:
            self.lost_screen.activate()

        pg.display.flip()

    def check_events(self):
        self.events = pg.event.get()
        for event in self.events:
            if event.type == QUIT:
                pg.quit()
                sys.exit(0)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not self.play_animation:
                    self.play_animation = True

                if self.global_flag.trigger_main_game:
                    if (event.key == pg.K_p and not self.paused_screen.run):
                        self.paused_screen.run = True
                        self.paused_screen.paused_time = pg.time.get_ticks()
                    if event.key == pg.K_w:
                        self.lost_screen.run = True

            if event.type in [WINDOWFOCUSLOST, WINDOWMOVED]:
                self.paused_screen.run = True
                self.paused_screen.paused_time = pg.time.get_ticks()

    def run(self):
        while 1:
            self.check_events()
            self.update()
            self.draw()
