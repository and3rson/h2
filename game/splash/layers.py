import cocos
from cocos.scenes.transitions import *
from time import sleep
from threading import Thread
from .. import menu
import pygame


class MainLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(MainLayer, self).__init__()

    def on_key_press(self, key, modifiers):
        # print key, modifiers
        trans = FadeTransition(
            cocos.scene.Scene(menu.MenuScene()), duration=1
        )
        cocos.director.director.replace(trans)
        # cocos.director.director.exit()
        # pyglet.app.exit()


class BackgroundLayer(cocos.layer.Layer):
    def __init__(self):
        super(BackgroundLayer, self).__init__()


class TextLayer(cocos.layer.Layer):
    def __init__(self):
        super(TextLayer, self).__init__()

        label = cocos.text.Label(
            'axeHead',
            font_name='Arial',
            font_size=24,
            anchor_x='center',
            anchor_y='center'
        )

        label.position = 320, 240

        self.add(label)

        # scale = cocos.actions.ScaleBy(2, duration=1)
        # label.do(cocos.actions.Repeat(scale + cocos.actions.Reverse(scale)))
        # label.do(cocos.actions.Repeat(scale + cocos.actions.Reverse(scale)))

        self.label = label

        w, h = cocos.director.director.get_window_size()

        # Axe box
        self.axe_box = cocos.cocosnode.CocosNode()
        self.axe_box.anchor = (0.5, 0)
        self.axe_box.position = w / 2, h / 2
        self.add(self.axe_box)

        # Axe
        self.axe = cocos.sprite.Sprite('res/sprites/axe.png')
        # print self.axe.anchor
        # self.axe.size = 32, 32
        self.axe.position = w / 3 * 2, 37.5 - 10
        self.axe.scale = 0.25
        self.axe_box.add(self.axe)

        animations = []
        for i in xrange(16, 0, -1):
            # animations.append(
            #     cocos.actions.Rotate(-i * 10, duration=0.05)
            # )
            animations.append(
                cocos.actions.Rotate(
                    i * (-1 if i % 2 else 1), duration=0.033
                )
            )

        self.axe.do(cocos.actions.Rotate(-720 - 135, duration=0.4))
        #      +
        #     cocos.actions.Rotate(8, duration=0.05) +
        #     cocos.actions.Rotate(-8, duration=0.05) +
        #     cocos.actions.Rotate(8, duration=0.05)
        # )
        self.axe.do(cocos.actions.MoveBy((-w / 3 * 2, 0), duration=0.4))

        whip = pygame.mixer.Sound('res/sounds/whip.ogg')
        whip.set_volume(0.7)
        whip.play()
        hit = pygame.mixer.Sound('res/sounds/hit.ogg')

        def do_hit():
            sleep(0.4)
            hit.play()
            p = self.axe.position
            self.axe_box.do(reduce(lambda x, y: x + y, animations))

        thread = Thread(target=do_hit)
        thread.start()
