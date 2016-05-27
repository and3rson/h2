import cocos
import layers


class SplashScene(cocos.scene.Scene):
    def __init__(self):
        super(SplashScene, self).__init__(
            layers.MainLayer()
        )
