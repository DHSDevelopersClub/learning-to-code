'''Lesson 1 - step 2.

Now we can move the image around.

TASKS:
    - Change the image to "paddle.jpg"
    - Rename all "kitten" variables to make more sense
    - Restrict motion in the y direction, so it stays 10 pixels 
      above the bottom of the screen, but follows the mouse in the 
      x direction.
'''

import pyglet


window = pyglet.window.Window()

kitten_image = pyglet.image.load('kitten.jpg')

# A `Sprite` is an object that controls an image.  It will allow us
# to easily move the image around.
kitten_sprite = pyglet.sprite.Sprite(kitten_image)

@window.event
def on_draw():
    window.clear()
    # We don't need to `blit` the kitten image anymore.  
    # `kitten_sprite` will take care of that, we just need to tell
    # it to draw itself, it knows it's own position.
    kitten_sprite.draw()

# When the window detects that the mouse has moved, it will run the
# indented code.
@window.event
# This time, it gives us some information.  `mouse_x` and `mouse_y`
# represent the new x, y position of the mouse.  Don't worry about 
# `dx` and `dy`, we won't be using them today.
def on_mouse_motion(mouse_x, mouse_y, dx, dy):
    # Change the x and y position of our kitten sprite.
    kitten_sprite.x = mouse_x
    kitten_sprite.y = mouse_y


pyglet.app.run()
