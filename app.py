#!/usr/bin/env python2

import sys

import cocos
import pygame
if sys.platform.startswith('win'):
    import pygame._view

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

import game.splash
import game.menu

cocos.director.director.init()
cocos.director.director.show_FPS = True
cocos.director.director.run(game.splash.SplashScene())
# cocos.director.director.run(game.menu.MenuScene())
