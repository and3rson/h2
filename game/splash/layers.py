import cocos
from cocos.scenes.transitions import *
from time import sleep
from threading import Thread
from .. import menu
import pygame


class MainLayer(cocos.layer.Layer):
    is_event_handler = True

    def on_key_press(self, key, modifiers):
        # print key, modifiers
        # print key
        if self.can_skip:
            self.end_scene()

    def end_scene(self):
            trans = FadeTransition(
                menu.MenuScene(), duration=1
            )
            cocos.director.director.replace(trans)
            self.can_skip = False
        # cocos.director.director.exit()
        # pyglet.app.exit()

    def __init__(self):
        super(MainLayer, self).__init__()

        self.can_skip = False

        label = cocos.text.Label(
            'splash?',
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

        self.do(cocos.actions.Delay(3) + cocos.actions.CallFunc(self.end_scene))

        whip = pygame.mixer.Sound('res/sounds/whip.ogg')
        whip.set_volume(0.7)
        whip.play()
        hit = pygame.mixer.Sound('res/sounds/hit.ogg')

        def do_hit():
            self.can_skip = True

            sleep(0.4)
            hit.play()
            self.axe_box.do(reduce(lambda x, y: x + y, animations))

        thread = Thread(target=do_hit)
        thread.start()
