import cocos
from random import random
import math
from threading import Thread, Lock
from time import time


class LightningGenerator(Thread):
    def __init__(self):
        Thread.__init__(self)

        self.result = None

    def _rotate_around_point(self, cx, cy, x, y, angle):
        radians = (math.pi / 180) * angle
        cos = math.cos(radians)
        sin = math.sin(radians)
        nx = (cos * (x - cx)) + (sin * (y - cy)) + cx
        ny = (cos * (y - cy)) - (sin * (x - cx)) + cy
        return nx, ny

    def _draw_step(self, start, attraction, limit, width, left):
        if limit <= 0:
            return []
        if width < 0.25:
            pass

        rotated = self._rotate_around_point(
            0, 0,
            attraction[0], attraction[1],
            random() * 45 * (-1 if left else 1)
        )
        end = (
            start[0] + rotated[0] * random() * 20,
            start[1] + rotated[1] * random() * 20
        )

        lines = [
            cocos.draw.Line(
                (start[0], start[1]),
                (end[0], end[1]),
                (255, 255, 255, 255),
                width
            )
        ]

        # self.lines.append(line)
        # self.add(line)

        if random() <= 0.05:
            rotated1 = self._rotate_around_point(
                0, 0,
                rotated[0], rotated[1],
                -22.5
            )
            rotated2 = self._rotate_around_point(
                0, 0,
                rotated[0], rotated[1],
                22.5
            )
            lines.extend(
                self._draw_step(
                    end, rotated1, limit - 2 * random(), width * 0.9, True
                )
            )
            lines.extend(
                self._draw_step(
                    end, rotated2, limit - 2 * random(), width * 0.9, False
                )
            )
        else:
            lines.extend(
                self._draw_step(
                    end, rotated, limit - 2 * random(), width * 0.9, not left
                )
            )
        return lines

    def run(self):
        start = time()

        w, h = cocos.director.director.get_window_size()

        # self.modification_lock.acquire()

        lines = self._draw_step((0, 0), (0, -1), 25, 5, random() >= 0.5)

        # self.modification_lock.release()

        self.result = lines

        # print 'Lightning generated in', time() - start, 's'


class LightningNode(cocos.cocosnode.CocosNode):
    def __init__(self):
        super(LightningNode, self).__init__()

        self.modification_lock = Lock()

        self.i = 0
        self.lines = []

        self.generator = None

        self.last_draw = 0

    def draw(self, *args, **kwargs):
        # if self.new_lines:
        #     for line in self.lines:
        #         line.kill()
        #     self.lines = self.new_lines
        #     for line in self.lines:
        #         self.add(line)
        #     self.new_lines = False

        if self.generator and self.generator.result:
            start = time()
            for line in self.lines:
                line.kill()
            self.lines = self.generator.result
            for line in self.lines:
                self.add(line)
            self.generator = None
            self.last_draw = time()
            w, h = cocos.director.director.get_window_size()
            # self.position = random() * w, h

        # print 'LightningNode.draw', args, kwargs
        super(LightningNode, self).draw(*args, **kwargs)

    def generate(self):
            self.generator = LightningGenerator()
            self.generator.start()
