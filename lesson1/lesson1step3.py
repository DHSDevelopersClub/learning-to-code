'''Lesson 1 - step 3.

Starting to look like a game of ping pong.

TASKS:
    - Improve all imports to be more specific.
      - pyglet.sprite.Sprite -> Sprite
      - pyglet.app.run -> run
'''

import pyglet
# This import is more specific.  We can now refer to 
# `pyglet.window.Window` as just `Window`.
from pyglet.window import Window
# With the `as` keyword, we can rename an import to make it more 
# clear.  If it were just `load`, it wouldn't be clear to a person 
# reading it that it is an image we are loading.
from pyglet.image import load as load_image


window = Window()

paddle_image = load_image('paddle.png')
# By default, the anchor is in the bottom left of the image (0, 0). 
# Setting `anchor_x` to half of the images width will make the 
# cursor control the image from the center.
paddle_image.anchor_x = paddle_image.width / 2

# We can set the starting position of the sprite to (0, 10).  
# Normally, it defaults to (0, 0)
paddle_sprite = pyglet.sprite.Sprite(paddle_image, 0, 10)

@window.event
def on_draw():
    window.clear()
    paddle_sprite.draw()

@window.event
def on_mouse_motion(mouse_x, mouse_y, dx, dy):
    # Calculate the furthest right we want our paddle to go.
    right_side = window.width - paddle_sprite.width / 2
    
    # If the mouse goes further than that, snap it back to the 
    # limit.  This won't change the actual position of the mouse 
    # pointer, it just changes the variable...
    if mouse_x > right_side:
        mouse_x = right_side
        
    # ...but the variable controls our paddle.
    paddle_sprite.x = mouse_x


pyglet.app.run()
