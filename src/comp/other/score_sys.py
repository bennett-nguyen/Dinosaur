import pygame as pg
import src.preload.ds as ds
import src.preload.assets as assets
import src.preload.constant as const
from src.preload.assets import CustomFont

class ScoreSys:
    def __init__(self, text_color: tuple[int, int, int]):
        self.font = CustomFont.get_font('PressStart2P', 20)
        self.padding = 25
        self.score_incrementer = 1
        self.current_color = text_color
        
        # animation
        self.animation_current_time = 0
        self.blink_time = 0
        self.activated_time = 0
        self.blink_delay = 200
        self.animation_play_time = 2000
        self.is_blinking = False
        

        self.current_time = 0
        self.incremented_score_time = 0
        self.delay = 90

        self.score = 0
        self.highest_score = 0
        self.score_length = 5

        self.reached_milestone = False
        self.is_playing_animation = False
        self.milestone_text = None

        self.score_text = self.font.render(f'{(self.score_length - len(str(self.score))) * "0"}{self.score}', True, self.current_color)
        self.score_rect = self.score_text.get_rect(topright=(const.WIDTH - self.padding, 0 + self.padding))
        self.highest_score_text = self.font.render(f'HI {self.compute_visual(self.highest_score)}', True, self.current_color)
        rect_x, rect_y = self.score_rect.midleft
        self.highest_score_rect = self.highest_score_text.get_rect(midright=(rect_x - self.padding, rect_y))

    def increment_score(self):
        self.current_time = pg.time.get_ticks()
        if self.current_time - self.incremented_score_time >= self.delay:
            self.score += self.score_incrementer

            self.score_text = self.font.render(f'{self.compute_visual(self.score)}', True, self.current_color)
            self.score_rect = self.score_text.get_rect(topright=(const.WIDTH - self.padding, 0 + self.padding))
            
            rect_x, rect_y = self.score_rect.midleft
            self.highest_score_rect = self.highest_score_text.get_rect(midright=(rect_x - self.padding, rect_y))
            self.incremented_score_time = self.current_time

            if self.score % (self.score_incrementer * 100) == 0:
                assets.Audio.REACHED_MILESTONE.play()
                self.milestone_text = self.score_text
                self.reached_milestone = True
                self.activated_time = pg.time.get_ticks()
                self.blink_time = pg.time.get_ticks()
    
    def redraw(self):
        if self.reached_milestone:
            self.milestone_animation()
            if not self.is_blinking:
                ds.screen.blit(self.milestone_text, self.score_rect)
        else:
            ds.screen.blit(self.score_text, self.score_rect)

        ds.screen.blit(self.highest_score_text, self.highest_score_rect)
    
    def update_color(self, color: tuple[int, int, int]):
        self.current_color = color
        self.highest_score_text = self.font.render(f'HI {self.compute_visual(self.highest_score)}', True, self.current_color)
        self.score_text = self.font.render(self.compute_visual(self.score), True, self.current_color)

    def compute_visual(self, score):
        prefix = ''
        if self.score_length - len(str(score)) > 0: 
            prefix = (self.score_length - len(str(score))) * "0"
        return f'{prefix}{score}'

    def milestone_animation(self):
        self.animation_current_time = pg.time.get_ticks()
        if self.current_time - self.activated_time >= self.animation_play_time:
            self.reached_milestone = False
            return

        if self.animation_current_time - self.blink_time >= self.blink_delay and not self.is_blinking:
            self.is_blinking = True
            self.blink_time = pg.time.get_ticks()
            return


        if self.animation_current_time - self.blink_time >= self.blink_delay:
            self.is_blinking = False
            self.blink_time = pg.time.get_ticks()