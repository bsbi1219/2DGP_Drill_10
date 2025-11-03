from pico2d import load_image, get_time, load_font

import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0) # Meter / Minute
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0) # Meter / Second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # pixel per second

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = 800, 450
        self.frame = 0
        self.dir = 1

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    def draw(self):
        if self.dir == 0:
            self.image.clip_draw(int(self.frame) * 183, 0, 183, 168, self.x, self.y, 70, 60)
        else:
            self.image.clip_composite_draw(int(self.frame) * 183, 0, 183, 168, 0, 'h', self.x, self.y, 70, 60)

    def update(self):
        pass