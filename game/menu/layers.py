import cocos
import pygame
import pyglet
# from cocos.scenes.transitions import *
from ..common.nodes import LightningNode


class MainLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(MainLayer, self).__init__()

        music = pygame.mixer.Sound('res/music/ChinaDoll.ogg')
        music.set_volume(0.7)
        music.play()

    def on_key_press(self, key, modifiers):
        if key in xrange(256) and chr(key) == 'q':
            pyglet.app.exit()


class LightningLayer(cocos.layer.ColorLayer):
    def __init__(self):
        super(LightningLayer, self).__init__(255, 255, 255, 0)
        w, h = cocos.director.director.get_window_size()

        self.lightning = LightningNode()
        self.lightning.layer = self
        self.lightning.position = w / 2, h
        self.add(self.lightning)


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
                cocos.actions.MoveBy((-self.sky.width / 2, 0), duration=15) +
                cocos.actions.MoveBy((self.sky.width / 2, 0), duration=0)
            )
        )
