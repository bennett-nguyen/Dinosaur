import pygame as pg
import src.preload.ds as ds
import src.preload.assets as assets
import src.preload.constant as const

from src.preload.comp import Timer
from src.comp.other.dino import Dino
from src.preload.shared import shared_data
# from src.comp.other.paused_screen import PausedScreen
from src.comp.other.score_sys import ScoreSys
from src.comp.other.background import Background
from src.comp.other.obstacle import ObstacleGenerator

class Game:
    def __init__(self):
        self.transform_to = None
        self.is_transforming_state = False
        self.done_transforming_text_color = False
        self.done_transforming_screen_color = False
        self.color_transitive_speed = 150
        self.update_color()

        self.ground = self.ground_2 = assets.Gallery.GROUND
        self.ground.get_state(shared_data.time_state)
        self.ground_2.get_state(shared_data.time_state)

        self.ground_rect = self.ground.current.get_rect(bottomleft = (0, const.HEIGHT - const.GROUND_POS_Y_OFFSET))
        self.ground_2_rect = self.ground_2.current.get_rect(bottomleft = (self.ground_rect.right, self.ground_rect.bottom))
        shared_data.GROUND_Y_VALUE = self.ground_rect.top + const.DINO_POS_Y_OFFSET

        # Services
        self.dino = Dino()
        self.score_sys = ScoreSys(self.message_color)
        self.background = Background()
        self.obstacles_generator = ObstacleGenerator()
        # self.paused_screen = PausedScreen() # this feature is still buggy
        
        # Timers
        self.cycle_delay = const.DAY_NIGHT_CYCLE_DELAY * 1000
        self.cycle_timer = Timer(self.cycle_delay)
        
        # Temporary stuff
        self.started = False
        self.step_counter = 0
        self.allow_keydown = True
        self.done_transforming_background = False
        self.done_transforming_dino = False
        start_font = assets.CustomFont.get_font('PressStart2P', 25)

        self.start_message = start_font.render("Press 'Space' to play", True, self.message_color)
        self.start_rect = self.start_message.get_rect(center = (const.HALF_WIDTH, const.HALF_HEIGHT))

        self.white_screen_1 = pg.Surface((self.dino.current_rect.left - 25, const.HEIGHT))
        self.white_screen_2 = pg.Surface((const.WIDTH - (self.dino.current_rect.right + 25), const.HEIGHT))

        self.white_screen_1.fill(self.screen_color)
        self.white_screen_2.fill(self.screen_color)

        self.white_screen_1_rect = self.white_screen_1.get_rect(topleft=(0, 0))
        self.white_screen_2_rect = self.white_screen_2.get_rect(topright=(const.WIDTH, 0))


    def update_color(self):
        if shared_data.time_state == const.DAY:
            self.message_color = tuple(const.DAY_MESSAGE_COLOR)
            self.screen_color = tuple(const.DAY_SCREEN_COLOR)
        elif shared_data.time_state == const.NIGHT:
            self.message_color = tuple(const.NIGHT_MESSAGE_COLOR)
            self.screen_color = tuple(const.NIGHT_SCREEN_COLOR)


    def apply_color(self):
        self.dino.get_obj_state()
        self.score_sys.update_color(self.message_color)

        if not self.done_transforming_background:
            self.white_screen_1.fill(self.screen_color)
            self.white_screen_2.fill(self.screen_color)
            start_font = assets.CustomFont.get_font('PressStart2P', 25)
            self.start_message = start_font.render("Press 'Space' to play", True, self.message_color)


    def redraw(self):
        ds.screen.blit(self.ground.current, self.ground_rect)
        ds.screen.blit(self.ground_2.current, self.ground_2_rect)

        self.background.draw_moon_n_stars()
        if self.done_transforming_dino:
            self.background.draw_clouds()
        self.score_sys.redraw()
        self.__draw_start_screen()

        if self.done_transforming_background:
            if self.done_transforming_dino:
                self.__move_ground()
                self.obstacles_generator.move_and_redraw_obstacle()
            else:
                self.__transform_dino()

        self.dino.redraw()
    
    def input(self):
        for event in shared_data.events:
            # fake jump animation at start screen
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not self.started:
                    assets.Audio.JUMP.play()
                    self.dino.player_state = 'jump'
                    self.dino.gravity = self.dino.default_gravity
                    self.is_jumping = True
                    self.started = True
                # if event.key == pg.K_p:
                #     self.paused_screen.run = True

    def update(self):
        # if self.check_collide():
        #     self.game_over()

        self.obstacles_generator.generate_object()
        if self.allow_keydown:
            self.input()
            if self.done_transforming_dino:
                # if self.paused_screen.run == True:
                #     paused_time = pg.time.get_ticks()
                    # self.paused_screen.paused_time = paused_time
                    # self.paused_screen.change_title_color(self.message_color)
                    # self.paused_screen.activate_pause_screen()
                self.day_night_cycle()
                self.dino.input()
                self.score_sys.increment_score()

        self.redraw()
        self.dino.apply_gravity()

    def check_collide(self):
        pass

    def game_over(self):
        pass

    def __move_ground(self):
        shared_data.velocity =  round((const.DINO_VELOCITY + shared_data.velocity_incrementer) * shared_data.dt)
        self.ground_rect.left -= shared_data.velocity
        self.ground_2_rect.left -= shared_data.velocity

        if self.ground_rect.right <= 0:
            self.ground_rect.left = self.ground_2_rect.right 
        elif self.ground_2_rect.right <= 0:
            self.ground_2_rect.left = self.ground_rect.right 

    def __draw_start_screen(self):
        if not self.started:
            ds.screen.blit(self.white_screen_1, self.white_screen_1_rect)
            ds.screen.blit(self.white_screen_2, self.white_screen_2_rect)
            ds.screen.blit(self.start_message, self.start_rect)

        if not self.done_transforming_background and self.started:
            ds.screen.blit(self.white_screen_1, self.white_screen_1_rect)
            ds.screen.blit(self.white_screen_2, self.white_screen_2_rect)
            self.__transform_background()

    def __transform_dino(self):
        if self.dino.current_rect.bottom >= shared_data.GROUND_Y_VALUE and self.step_counter <= const.DINO_POS_X_OFFSET:
            self.allow_keydown = False
            self.dino.current_rect.x += 1
            self.step_counter += 1

        elif self.step_counter > const.DINO_POS_X_OFFSET:
            self.allow_keydown = True
            self.done_transforming_dino = True
            self.dino.current_rect = self.dino.current_rect
            delattr(self, 'step_counter')
            delattr(self.dino, 'fake_rect')


    def __transform_background(self):
        self.white_screen_1_rect.x -= 5
        self.white_screen_2_rect.x += 40

        if self.white_screen_1_rect.right <= 0 and self.white_screen_2_rect.left >= const.WIDTH:
            self.done_transforming_background = True
            delattr(self, 'white_screen_1')
            delattr(self, 'white_screen_2')
            delattr(self, 'white_screen_1_rect')
            delattr(self, 'white_screen_2_rect')
            delattr(self, 'start_message')
            delattr(self, 'start_rect')

    def day_night_cycle(self):
        self.cycle_timer.set_current_time()
        if not self.cycle_timer.static_point: self.cycle_timer.set_static_point()

        if self.cycle_timer.timer() and not self.is_transforming_state:
            self.transform_to = const.NIGHT if shared_data.time_state == const.DAY else const.DAY
            self.is_transforming_state = True
            self.cycle_timer.set_static_point()

        if self.is_transforming_state:
            if self.transform_to == const.DAY:
                self.__transform_day()

            elif self.transform_to == const.NIGHT:
                self.__transform_night()

        if self.done_transforming_screen_color and self.done_transforming_text_color:
            self.is_transforming_state = False
            self.done_transforming_screen_color = False
            self.done_transforming_text_color = False
            shared_data.time_state = self.transform_to

    def __transform_day(self):
        screen_r, screen_g, screen_b = self.screen_color
        mess_r, mess_g, mess_b = self.message_color

        speed = round(self.color_transitive_speed * shared_data.dt)

        if not self.done_transforming_screen_color:
            screen_r += speed
            screen_g += speed
            screen_b += speed

            if screen_r >= const.DAY_SCREEN_COLOR.R // 2: self.__change_state_at_half_rgb()
            if screen_r >= const.DAY_SCREEN_COLOR.R:
                self.done_transforming_screen_color = True
                screen_r, screen_g, screen_b = const.DAY_SCREEN_COLOR

        if not self.done_transforming_text_color:
            speed = round(self.color_transitive_speed * shared_data.dt)
            mess_r -= speed
            mess_b -= speed
            mess_g -= speed

            if mess_r <= const.DAY_MESSAGE_COLOR.R:
                self.done_transforming_text_color = True
                mess_r, mess_g, mess_b = const.DAY_MESSAGE_COLOR

        self.screen_color = (screen_r, screen_g, screen_b)
        self.message_color = (mess_r, mess_g, mess_b)

    def __transform_night(self):
        screen_r, screen_g, screen_b = self.screen_color
        mess_r, mess_g, mess_b = self.message_color

        speed = round(self.color_transitive_speed * shared_data.dt)

        if not self.done_transforming_screen_color:
            screen_r -= speed
            screen_g -= speed
            screen_b -= speed

            if screen_r <= const.DAY_SCREEN_COLOR.R // 2: self.__change_state_at_half_rgb()
            if screen_r <= const.NIGHT_SCREEN_COLOR.R:
                self.done_transforming_screen_color = True
                screen_r, screen_g, screen_b = const.NIGHT_SCREEN_COLOR

        if not self.done_transforming_text_color:
            mess_r += speed
            mess_b += speed
            mess_g += speed
            if mess_r >= const.NIGHT_MESSAGE_COLOR.R:
                self.done_transforming_text_color = True
                mess_r, mess_g, mess_b = const.NIGHT_MESSAGE_COLOR

        self.screen_color = (screen_r, screen_g, screen_b)
        self.message_color = (mess_r, mess_g, mess_b)

    def __change_state_at_half_rgb(self):
        shared_data.time_state = self.transform_to
        self.ground.get_state(shared_data.time_state)
        self.ground_2.get_state(shared_data.time_state)
