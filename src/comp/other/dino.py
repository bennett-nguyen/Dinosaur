import pygame as pg
import src.preload.ds as ds
import src.preload.assets as assets
import src.preload.constant as const
from src.preload.comp import MultiTimer
from src.preload.shared import shared_data

class Dino:
    def __init__(self):
        self.player_state = const.IDLE
        self.gravity = 0
        self.default_gravity = -30
        self.gravity_incrementer = 2

        self.dino_idle = self.dino_jump = assets.Gallery.DINO_IDLE
        self.dino_running = (assets.Gallery.DINO_RUNNING_1, assets.Gallery.DINO_RUNNING_2)
        self.dino_duck = (assets.Gallery.DINO_DUCK_1, assets.Gallery.DINO_DUCK_2)
        self.dino_blink = assets.Gallery.DINO_BLINK
        self.dino_dead = assets.Gallery.DINO_DEAD


        self.image = self.dino_idle

        self.fake_rect = self.image.current.get_rect(midbottom=(100, shared_data.GROUND_Y_VALUE)) # for dino transforming
        self.rect = self.image.current.get_rect(midbottom=(self.fake_rect.centerx + const.DINO_POS_X_OFFSET, shared_data.GROUND_Y_VALUE))
        self.duck_rect = self.dino_duck[0].current.get_rect(midbottom=(self.rect.centerx + 10, shared_data.GROUND_Y_VALUE))

        self.current_rect = self.fake_rect

        # -- Animation stuff
        # idle
        self.is_blinking = False
        self.blink_delay = 7000 # how long you want the dino to stay unblink
        self.blinking_time = 200 # how long you want the dino to blink
        self.blink_multitimer = MultiTimer([self.blink_delay, self.blinking_time])

        # running & dodge
        self.index = 0
        self.animation_speed = 10
        self.is_ducking = False

        # jump
        self.is_jumping = False

    def redraw(self):
        self._check_player_state()
        ds.screen.blit(self.image.current, self.current_rect)

    def get_obj_state(self):
        self.image.get_state(shared_data.time_state)

    def input(self):
        for event in shared_data.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and self.current_rect.bottom >= shared_data.GROUND_Y_VALUE and not self.is_ducking:
                        assets.Audio.JUMP.play()
                        self.is_jumping = True
                        self.player_state = const.JUMP
                        self.gravity = self.default_gravity
                elif event.key == pg.K_DOWN:
                    if not self.is_jumping:
                        self.player_state = const.DUCK
                        self.is_ducking = True
                    else:
                        self.gravity_incrementer = 7

            if event.type == pg.KEYUP and event.key == pg.K_DOWN and not self.is_jumping:
                self.player_state = const.RUN
                self.current_rect = self.rect
                self.is_ducking = False


    def apply_gravity(self):
        self.gravity += self.gravity_incrementer
        self.current_rect.y += self.gravity
        if self.current_rect.bottom >= shared_data.GROUND_Y_VALUE:
            self.current_rect.bottom = shared_data.GROUND_Y_VALUE
            self.is_jumping = False
            self.gravity_incrementer = 2

    def _check_player_state(self):
        if shared_data.is_lose:
            self._dead_animation()
            return

        match self.player_state:
            case const.IDLE:
                if not self.blink_multitimer.static_point:
                    self.blink_multitimer.set_static_point()
                self._idle_animation()
            case const.JUMP:
                self._jump_animation()
            case const.RUN:
                self._running_animation()
            case const.DUCK:
                self._duck_animation()

    def _idle_animation(self):
        self.blink_multitimer.set_current_time()

        if self.blink_multitimer.timer() and not self.is_blinking:
            self.is_blinking = True
            self.image = self.dino_blink
            self.blink_multitimer.set_current_time()
            self.blink_multitimer.set_static_point()
            self.blink_multitimer.switch_timer()
            return

        if self.blink_multitimer.timer() and self.is_blinking:
            self.is_blinking = False
            self.image = self.dino_idle
            self.blink_multitimer.set_current_time()
            self.blink_multitimer.set_static_point()
            self.blink_multitimer.switch_timer()

    def _jump_animation(self):
        if self.is_jumping:
            self.image = self.dino_jump
            return

        self.player_state = const.RUN

    def _running_animation(self):
        if shared_data.allow_animation:
            self.index += self.animation_speed * shared_data.dt
            if self.index >= len(self.dino_running):
                self.index = 0

        self.image = self.dino_running[int(self.index)]

    def _duck_animation(self):
        if shared_data.allow_animation:
            self.index += self.animation_speed * shared_data.dt
            if self.index >= len(self.dino_running):
                self.index = 0

        self.image = self.dino_duck[int(self.index)]
        self.current_rect = self.duck_rect

    def _dead_animation(self):
        self.image = self.dino_dead
        self.current_rect = self.rect
    
    def reset(self):
        self.is_ducking = False
        self.is_jumping = False
        self.current_rect.bottom = shared_data.GROUND_Y_VALUE
        self.player_state = const.RUN
        self.index = 0
        self.gravity = 0
        self.gravity_incrementer = 2