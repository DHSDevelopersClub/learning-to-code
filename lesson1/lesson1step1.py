'''Lesson 1 - step 1.

Just getting started making a window and drawing to it.

This is a docstring, short for documentation string.  This is the
place where you describe what the file is for, so a human reading
your code can have an easier time.

TASKS:
    - Rename `kitten_image` to `puppy_image`.
    - Change the image to "puppy.jpg".
'''

# Pyglet allows us to create windows and draw things to those
# windows.  It isn't build into python, so we need to import it in
# order to use it.
import pyglet


# Create a new window, using pyglet, and name it `window`.
window = pyglet.window.Window()

# Load the image "kitten.jpg" with pyglet, and name it
# `kitten_image`.
kitten_image = pyglet.image.load('kitten.jpg')

# When `window` decides it needs to redraw (flip to a new page in
# the flip book), it will run the indented code.
@window.event
def on_draw():
    # Tell `window` to clear away the previous frame.
    window.clear()
    # `blit` means draw.  We are telling our `kitten_image` to draw
    # itself at the point (0, 0).
    kitten_image.blit(0, 0)

# Tell pyglet that our game is ready to run.
pyglet.app.run()
