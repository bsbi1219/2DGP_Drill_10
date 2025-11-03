from pico2d import load_image, get_time, load_font

import game_world
import game_framework
from state_machine import StateMachine

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = 800, 450
        self.frame = 0