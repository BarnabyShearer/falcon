#! /usr/bin/env python3
"""
Simulate a gun's recoil when you pull the trigger.
"""

import pyglet

from falcon import buttons, falcon, vec, xyz

FORCE = [0, 10, 10]
DURATION = 4

old_buttons = 0
recoil = 0

all = None
sight = None
bang = None

def main():
    window = pyglet.window.Window(fullscreen=True)

    loading = pyglet.text.Label(
        'Loading…',
        x=window.width // 2,
        y=window.height // 2,
        anchor_x='center',
        anchor_y='center'
    )

    background = pyglet.graphics.vertex_list(
        4,
        ('v2i', (
            0, 0,
            window.width, 0,
            window.width, window.height,
            0, window.height
        )),
        ('c3B', (
            0, 0xFF, 0,
            0, 0xFF, 0,
            0, 0, 0xFF,
            0, 0, 0xFF
        ))
    )

    f = falcon()

    @window.event
    def on_draw():
        background.draw(pyglet.gl.GL_QUADS)
        if all:
            all.draw()
        else:
            loading.draw()

    @window.event
    def on_key_press(symbol, modifiers):
        pyglet.app.event_loop.exit()

    def update(dt):
        global old_buttons, recoil, all, sight, bang

        if not all:
            _all = pyglet.graphics.Batch()
            sight = pyglet.sprite.Sprite(pyglet.image.load('sight.gif'), batch=_all)
            bang = pyglet.resource.media('bang.wav', streaming=False)
            all = _all

        ff = next(f)

        if recoil > 0:
            recoil -= 1
            ff.setForces(vec(FORCE))
        else:
            ff.setForces(vec([0, 0, 0]))

        x, y, z = xyz(ff.getPosition())
        sight.x = window.width // 2 + x * window.width // 0.06
        sight.y = window.height // 2 + y * window.width // 0.06

        new_buttons = buttons(ff)
        if new_buttons & 1<<2 and not old_buttons & 1<<2:
            recoil = DURATION
            bang.play()
        if new_buttons & 1<<3:
            print("▶ pressed; exiting")
            pyglet.app.event_loop.exit()
        old_buttons = new_buttons

    pyglet.clock.schedule_interval(update, 1/60.)

    pyglet.app.run()

if __name__ == "__main__":
    main()
