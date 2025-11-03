from pico2d import load_image, get_time, load_font

import game_world
import game_framework
from state_machine import StateMachine

PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0) # Meter / Minute
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0) # Meter / Second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # pixel per second

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = 800, 450
        self.frame = 0
        self.dir = 0

    def draw(self):
        pass