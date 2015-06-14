'''Lesson 1 - complete.

Example of a completed lesson 1.
'''

from pyglet.window import Window
from pyglet.image import load as load_image
from pyglet.sprite import Sprite
from pyglet.app import run


window = Window()

paddle_image = load_image('paddle.png')
paddle_image.anchor_x = paddle_image.width / 2

paddle_sprite = Sprite(paddle_image, 0, 10)

@window.event
def on_draw():
    window.clear()
    paddle_sprite.draw()
    
@window.event
def on_mouse_motion(mouse_x, mouse_y, dx, dy):
    right_side = window.width - paddle_image.width / 2
    left_side = paddle_image.width / 2
    
    if mouse_x > right_side:
        mouse_x = right_side
    if mouse_x < left_side:
        mouse_x = left_side
        
    paddle_sprite.x = mouse_x


run()
