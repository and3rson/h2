import cocos
import cocos.particle_systems
import pygame
import pyglet
import math
from time import time
from random import random
# from cocos.scenes.transitions import *
from ..common.nodes import LightningNode
from ..common.particles import Rain


class MainLayer(cocos.layer.Layer):
    is_event_handler = True
    music = pygame.mixer.Sound('res/music/ChinaDoll.ogg')

    def __init__(self):
        super(MainLayer, self).__init__()

        MainLayer.music.set_volume(0.7)
        MainLayer.music.play()

    def on_key_press(self, key, modifiers):
        if key in xrange(256) and chr(key) == 'q':
            pyglet.app.exit()


class LightningLayer(cocos.layer.ColorLayer):
    def __init__(self):
        super(LightningLayer, self).__init__(255, 255, 255, 0)
        w, h = cocos.director.director.get_window_size()

        self.last_draw = 0

        self.lightning = LightningNode()
        self.lightning.position = w / 2, h
        self.add(self.lightning)

        self.rain = Rain(w, h)
        self.rain.position = w / 2, h
        self.add(self.rain)

        self.next_lightning = 0

    def draw(self):
        time_passed = time() - self.last_draw

        if time_passed < 0.3:
            opacity = int((math.sin(time_passed * math.pi * 20) + 1) / 2 * 255)
        else:
            opacity = 0
        self.lightning.visible = opacity > 128
        self.opacity = opacity / 2

        if self.next_lightning <= time():
            w, h = cocos.director.director.get_window_size()
            self.lightning.position = random() * w / 2 + w / 4, h
            self.lightning.generate()
            self.last_draw = time()
            self.next_lightning = time() + 1 + random() * 4

        super(LightningLayer, self).draw()


class BackgroundLayer(cocos.layer.scrolling.ScrollableLayer):
    def __init__(self):
        super(BackgroundLayer, self).__init__()

        w, h = cocos.director.director.get_window_size()

        self.sky = cocos.sprite.Sprite('res/sprites/sky.png', anchor=(0, 0))
        k = float(h) / self.sky.height
        self.sky.scale = k
        self.sky.position = 0, 0
        self.add(self.sky)

        self.do(
            cocos.actions.Repeat(
                cocos.actions.MoveBy((-self.sky.width / 2, 0), duration=30) +
                cocos.actions.MoveBy((self.sky.width / 2, 0), duration=0)
            )
        )
