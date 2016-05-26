import cocos
import layers


class MenuScene(cocos.scene.Scene):
    def __init__(self):
        super(MenuScene, self).__init__(
            layers.MainLayer(),
            layers.BackgroundLayer(),
        )
