import pygame as pg
import src.preload.ds as ds
from src.preload.shared import shared_data
import src.preload.assets as assets
import src.preload.constant as const

class Dino:
    def __init__(self, ground_rect: pg.Rect):
        self.ground_rect = ground_rect
        self.ground_pos = self.ground_rect.top + const.DINO_POS_Y_OFFSET
        self.time_state = 'day'
        self.player_state = 'idle' # 'idle', 'running', 'jump', 'dodge', 'dead'
        self.gravity = 0
        self.gravity_incrementer = 2

        self.dino_idle = self.dino_jump = assets.Gallery.DINO_IDLE
        self.dino_running = [assets.Gallery.DINO_RUNNING_1, assets.Gallery.DINO_RUNNING_2]
        self.dino_dodge = [assets.Gallery.DINO_DODGE_1, assets.Gallery.DINO_DODGE_2]
        self.dino_blink = assets.Gallery.DINO_BLINK
        self.dino_dead = assets.Gallery.DINO_DEAD
        
        self.image = self.dino_idle

        self.fake_rect = self.image.current.get_rect(midbottom=(100, self.ground_pos)) # for dino transforming
        self.rect = self.image.current.get_rect(midbottom=(self.fake_rect.centerx + const.DINO_POS_X_OFFSET, self.ground_pos))
        self.dodge_rect = self.dino_dodge[0].current.get_rect(midbottom=(self.rect.centerx + 10, self.ground_pos))

        self.current_rect = self.fake_rect
        # Animation stuff

        # idle
        self.current_time = 0
        self.blink_activated_time = 0
        self.is_blinking = False
        self.blink_delay = 5000
        self.blinking_time = 200

        # running & dodge
        self.index = 0
        self.velocity = 10
        self.speed = 0.2
        self.is_dodging = False

        # jump
        self.is_jumping = False
    def redraw(self):
        self._check_player_state()
        ds.screen.blit(self.image.current, self.current_rect)
    
    def get_obj_state(self):
        self.image.get_state(self.time_state)
    
    def input(self):
        for event in shared_data.events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and self.current_rect.bottom >= self.ground_pos and not self.is_dodging:
                        assets.Audio.JUMP.play()
                        self.is_jumping = True
                        self.player_state = 'jump'
                        self.gravity = -40
                elif event.key == pg.K_DOWN:
                    if not self.is_jumping:
                        self.player_state = 'dodge'
                        self.is_dodging = True

            if event.type == pg.KEYUP and event.key == pg.K_DOWN and not self.is_jumping:
                self.player_state = 'running'
                self.current_rect = self.rect
                self.is_dodging = False


    def apply_gravity(self):
        self.gravity += self.gravity_incrementer
        self.current_rect.y += self.gravity
        if self.current_rect.bottom >= self.ground_pos:
            self.current_rect.bottom = self.ground_pos
            self.is_jumping = False

    def _check_player_state(self):
        match self.player_state:
            case 'idle':
                if not self.blink_activated_time: self.blink_activated_time = pg.time.get_ticks()
                self._idle_animation()
            case 'jump':
                self._jump_animation()
            case 'running':
                self._running_animation()
            case 'dodge':
                self._dodge_animation()
    
    def _idle_animation(self):
        self.current_time = pg.time.get_ticks()
        
        if self.current_time - self.blink_activated_time >= self.blink_delay and not self.is_blinking:
            self.is_blinking = True
            self.image = self.dino_blink
            self.blink_activated_time = self.current_time = pg.time.get_ticks()
            return

        if self.current_time - self.blink_activated_time >= self.blinking_time and self.is_blinking:
            self.is_blinking = False
            self.image = self.dino_idle
            self.blink_activated_time = self.current_time = pg.time.get_ticks()

    def _jump_animation(self):
        if self.is_jumping:
            self.image = self.dino_jump
            return

        self.player_state = 'running'

    def _running_animation(self):
        self.index += self.speed
        if self.index >= len(self.dino_running):
            self.index = 0

        self.image = self.dino_running[int(self.index)]
    
    def _dodge_animation(self):
        self.index += self.speed
        if self.index >= len(self.dino_running):
            self.index = 0

        self.image = self.dino_dodge[int(self.index)]
        self.current_rect = self.dodge_rect