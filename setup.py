#!/usr/bin/env python2

import cx_Freeze
executables = [cx_Freeze.Executable("app.py")]

cx_Freeze.setup(
    name="H2",
    version="1",
    options=dict(
        build_exe=dict(
            packages=[
                "pyglet",
                "cocos",
                "pygame",
                "numpy"
            ],
            include_files=[
                'res'
            ]
        )
    ),
    executables=executables
)
