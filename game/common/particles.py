import cocos
from cocos.particle import ParticleSystem, Color
from cocos.euclid import Point2
import pyglet


class Rain(ParticleSystem):
    def __init__(self, w, h):
        ParticleSystem.__init__(self, False)
        self.pos_var = Point2(w, 0)
        self.speed = h * 3.5
        self.speed_var = h * 2.5

    texture = pyglet.resource.image('res/particles/rain2.png').texture


    # def load_texture(self):
    #     return pyglet.image.load('res/particles/rain.png').texture

    # total paticles
    total_particles = 2000

    # duration
    duration = -1

    # gravity
    gravity = Point2(0, -100)

    # angle
    angle = -105.0
    angle_var = 0

    # speed of particles
    # speed = 300.0
    # speed_var = 0.0

    # radial
    # radial_accel = -380
    # radial_accel_var = 0

    # tangential
    # tangential_accel = 45.0
    # tangential_accel_var = 0.0

    # emitter variable position
    # pos_var = Point2(100, 0)

    # life of particles
    life = 12.0
    life_var = 0.0

    # emits per frame
    emission_rate = total_particles / life

    # color of particles
    start_color = Color(1, 1, 1, 0.5)
    # start_color_var = Color(0, 0, 0, 0.0)
    end_color = Color(1, 1, 1, 0)
    # end_color_var = Color(0, 0, 0, 0, 0.0)

    # size, in pixels
    size = 20.0
    size_var = 10.0

    # blend additive
    blend_additive = True

    # color modulate
    # color_modulate = True
