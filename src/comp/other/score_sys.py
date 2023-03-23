import pygame as pg
import src.preload.assets as assets

from src.preload.utilities import Timer
from src.preload.settings import *
from src.preload.assets import CustomFont


class ScoreSys:
    def __init__(self, game):
        self.game = game
        self.font = CustomFont.get_font('PressStart2P', 20)
        self.padding = 25
        self.score_incrementer = 1
        self.current_color = self.game.background.text_color

        # Flag
        self.is_blinking = False
        self.reached_milestone = False

        # Timer
        self.delay = 90
        self.delay_modifier = 0
        self.blink_delay = 200
        self.animation_play_time = 2000

        self.score_timer = Timer(self.delay)
        self.blink_animation_timer = Timer(self.blink_delay)
        self.animation_timer = Timer(self.animation_play_time)

        # Score
        self.score = 0
        self.highest_score = 0
        self.score_length = 5

        # Images
        self.score_text = self.font.render(self._compute_visual(self.score), True, self.current_color)
        self.score_rect = self.score_text.get_rect(topright=(WIDTH - self.padding, 0 + self.padding))
        self.highest_score_text = self.font.render(f'HI {self._compute_visual(self.highest_score)}', True, self.current_color)
        rect_x, rect_y = self.score_rect.midleft
        self.highest_score_rect = self.highest_score_text.get_rect(midright=(rect_x - self.padding, rect_y))
        self.milestone_text = None

    def increment_score(self):
        self.score_timer.set_current_time()
        self.animation_timer.set_current_time()

        if self.score_timer.timer(length_buffer=-self.delay_modifier):
            self.score += self.score_incrementer
            self.score_timer.set_static_point()

            text = self._compute_visual(self.score)
            self.score_text = self.font.render(f'{text}', True, self.current_color)

            if len(text) > self.score_length:
                self.score_rect = self.score_text.get_rect(topright=(WIDTH - self.padding, 0 + self.padding))
                self.highest_score_rect.right = self.score_rect.left - self.padding

            if self.score % (self.score_incrementer * 100) == 0 and not self.reached_milestone:
                self._reached_milestone_event(text)

    def redraw(self):
        if self.reached_milestone:
            if not self.game.global_flag.trigger_subprocess:
                self._milestone_animation()

            if not self.is_blinking:
                self.milestone_text = self.font.render(f'{self.milestone_text_string}', True, self.current_color)
                self.game.screen.blit(self.milestone_text, self.score_rect)
        else:
            self.game.screen.blit(self.score_text, self.score_rect)

        self.game.screen.blit(self.highest_score_text, self.highest_score_rect)

    def update(self):
        if not self.game.global_flag.trigger_subprocess:
            self.increment_score()
        self.redraw()

    def _reached_milestone_event(self, text):
        self.game.modifier.dist_increment = min(self.game.modifier.dist_increment + 20, 500)
        self.game.modifier.vel_increment = min(self.game.modifier.dist_increment + 70, 1000)
        self.delay_modifier = min(self.delay_modifier + 2, 50)

        assets.Audio.REACHED_MILESTONE.play()
        self.milestone_text = self.score_text
        self.milestone_text_string = text
        self.reached_milestone = True
        self.blink_animation_timer.set_static_point()
        self.animation_timer.set_static_point()

    def change_state(self):
        color = DAY_TEXT_COLOR if self.game.time_state == DAY else NIGHT_TEXT_COLOR
        self.current_color = color
        self.highest_score_text = self.font.render(f'HI {self._compute_visual(self.highest_score)}', True, self.current_color)
        self.score_text = self.font.render(self._compute_visual(self.score), True, self.current_color)

    def _compute_visual(self, score: int) -> str:
        prefix = ''
        if self.score_length - len(str(score)) > 0:
            prefix = (self.score_length - len(str(score))) * "0"
        return f'{prefix}{score}'

    def _milestone_animation(self):
        self.blink_animation_timer.set_current_time()

        if self.animation_timer.timer():
            self.reached_milestone = False
            self.animation_timer.reset_paused_delay()
            return

        if self.blink_animation_timer.timer() and not self.is_blinking:
            self.is_blinking = True
            self.blink_animation_timer.set_static_point()
            return

        if self.blink_animation_timer.timer():
            self.is_blinking = False
            self.blink_animation_timer.set_static_point()

    def reset(self):
        self.current_color = DAY_TEXT_COLOR if self.game.time_state == DAY else NIGHT_TEXT_COLOR
        self.highest_score = max(self.score, self.highest_score)
        self.delay_modifier = 0
        self.score = 0

        self.score_text = self.font.render(self._compute_visual(self.score), True, self.current_color)
        self.score_rect = self.score_text.get_rect(topright=(WIDTH - self.padding, 0 + self.padding))
        rect_x, rect_y = self.score_rect.midleft
        self.highest_score_text = self.font.render(f'HI {self._compute_visual(self.highest_score)}', True, self.current_color)
        self.highest_score_rect = self.highest_score_text.get_rect(midright=(rect_x - self.padding, rect_y))
