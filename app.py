#!/usr/bin/env python2

import sys

import cocos
from game.common.layers import PythonLayer
cocos.layer.PythonInterpreterLayer.cfg = PythonLayer.cfg

import pygame
if sys.platform.startswith('win'):
    import pygame._view

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

import game.splash
import game.menu
from game.common.db import DB

# print DB.get('config').data.get('show_fps')
# DB.get('config').data['show_fps'] = 333

cocos.director.director.init()
cocos.director.director.show_FPS = DB.get('config').data.get('show_fps')
cocos.director.director.run(game.splash.SplashScene())
# cocos.director.director.run(game.menu.MenuScene())
