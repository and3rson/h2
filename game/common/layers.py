import cocos


class PythonLayer(cocos.layer.PythonInterpreterLayer):
    cfg = {
        'code.font_name': 'Monospace',
        'code.color': (255, 255, 255, 255),
        'code.font_size': 12,
        'caret.color': (255, 255, 255)
    }

    def __init__(self):
        super(PythonLayer, self).__init__()
