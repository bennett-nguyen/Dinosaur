import pygame as pg
import src.preload.ds as ds
import src.preload.assets as assets
import src.preload.constant as const

from src.preload.comp import Timer
from src.preload.assets import CustomFont
from src.preload.shared import shared_data

class ScoreSys:
    def __init__(self, text_color: tuple[int, int, int]):
        self.font = CustomFont.get_font('PressStart2P', 20)
        self.padding = 25
        self.score_incrementer = 1
        self.current_color = text_color
        
        self.score_incrementer_subtractor_delay = 0

        # Timer
        self.delay = 90
        self.blink_delay = 200
        self.animation_play_time = 2000
        self.is_blinking = False

        self.score_timer = Timer(self.delay)
        self.animation_play_time_timer = Timer(self.animation_play_time)
        self.blink_animation_timer = Timer(self.blink_delay)

        self.score = 0
        self.highest_score = 0
        self.score_length = 5

        self.reached_milestone = False
        self.is_playing_animation = False
        self.milestone_text = None

        self.score_text = self.font.render(self.compute_visual(self.score), True, self.current_color)
        self.score_rect = self.score_text.get_rect(topright=(const.WIDTH - self.padding, 0 + self.padding))
        self.highest_score_text = self.font.render(f'HI {self.compute_visual(self.highest_score)}', True, self.current_color)
        rect_x, rect_y = self.score_rect.midleft
        self.highest_score_rect = self.highest_score_text.get_rect(midright=(rect_x - self.padding, rect_y))

    def increment_score(self):
        self.score_timer.set_current_time()
        self.animation_play_time_timer.set_current_time()

        if self.score_timer.timer(self.score_timer.length_of_timer - self.score_incrementer_subtractor_delay):
            self.score += self.score_incrementer
            
            text = self.compute_visual(self.score)

            self.score_text = self.font.render(f'{text}', True, self.current_color)
            if len(text) > self.score_length: self.score_rect = self.score_text.get_rect(topright=(const.WIDTH - self.padding, 0 + self.padding))

            self.highest_score_rect.right = self.score_rect.left - self.padding
            self.score_timer.set_static_point()

            if self.score % (self.score_incrementer * 100) == 0 and not self.reached_milestone:
                shared_data.distance_incrementer = min(shared_data.distance_incrementer + 20, 500)
                shared_data.velocity_incrementer = min(shared_data.velocity_incrementer + 70, 1000)
                self.score_incrementer_subtractor_delay = min(self.score_incrementer_subtractor_delay + 2, 50)

                assets.Audio.REACHED_MILESTONE.play()
                self.milestone_text = self.score_text
                self.milestone_text_string = text
                self.reached_milestone = True
                self.blink_animation_timer.set_static_point()
                self.animation_play_time_timer.set_static_point()
    
    def redraw(self):
        if self.reached_milestone:
            self.milestone_animation()
            if not self.is_blinking:
                self.milestone_text = self.font.render(f'{self.milestone_text_string}', True, self.current_color)
                ds.screen.blit(self.milestone_text, self.score_rect)
        else:
            ds.screen.blit(self.score_text, self.score_rect)

        ds.screen.blit(self.highest_score_text, self.highest_score_rect)
    
    def update_color(self, color: tuple[int, int, int]):
        self.current_color = color
        self.highest_score_text = self.font.render(f'HI {self.compute_visual(self.highest_score)}', True, self.current_color)
        self.score_text = self.font.render(self.compute_visual(self.score), True, self.current_color)

    def compute_visual(self, score: int) -> str:
        prefix = ''
        if self.score_length - len(str(score)) > 0: 
            prefix = (self.score_length - len(str(score))) * "0"
        return f'{prefix}{score}'

    def milestone_animation(self):
        self.blink_animation_timer.set_current_time()

        if self.animation_play_time_timer.timer():
            self.reached_milestone = False
            return

        if self.blink_animation_timer.timer() and not self.is_blinking:
            self.is_blinking = True
            self.blink_animation_timer.set_static_point()
            return

        if self.blink_animation_timer.timer():
            self.is_blinking = False
            self.blink_animation_timer.set_static_point()
    
    def reset(self):
        self.highest_score = max(self.score, self.highest_score)
        self.score = 0
