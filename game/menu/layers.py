import cocos


class MainLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(MainLayer, self).__init__()

    def on_key_press(self, key, modifiers):
        pass


class BackgroundLayer(cocos.layer.Layer):
    def __init__(self):
        super(BackgroundLayer, self).__init__()

    def on_key_press(self, key, modifiers):
        pass
