'''Lesson 2 - step 1.

Getting started with moving objects.

TASKS:
    - Change the starting position and velocity of the ball
    - Change the update rate to 30, then 15 times per second.  Find a
      framerate that looks good.
    - The statement `x = x + y` can be rewritten to `x += y`.  It is
      easier to read as well as write.  Change statements to `+=`
      where possible.
    OR
    - Adapt this code to work with your own game.
'''

from pyglet.window import Window
from pyglet.image import load as load_image
from pyglet.sprite import Sprite
# `schedule_interval` allows us to repeatedly execute code.  We will
# use `schedule_interval` to update the position of the ping-pong
# ball 60 times a second.
from pyglet.clock import schedule_interval
from pyglet.app import run

# A `Vector` is just a way to store x, y pairs together.  It can be
# used to represent either positon or velocity.
from physics.vector import Vector


window = Window()

paddle_image = load_image('paddle.png')
paddle_image.anchor_x = paddle_image.width / 2
paddle_sprite = Sprite(paddle_image, 0, 10)

# Just like with the paddle, we load the ball image, then make it
# into a sprite.
ball_image = load_image('ball.png')
ball_sprite = Sprite(ball_image, 10, 300)
# Velocity is just speed with direction.  We use vectors to represent
# velocities.  `Vector()` creates a blank vector, with x and y both
# set to 0.
ball_velocity = Vector()
# The ball will move 50 pixels to the right every second.
ball_velocity.x = 50
# The ball will move 50 pixels down per second.
ball_velocity.y = -50

@window.event
def on_draw():
    window.clear()
    paddle_sprite.draw()
    # We draw the ball just like we do the paddle.
    ball_sprite.draw()

@window.event
def on_mouse_motion(mouse_x, mouse_y, dx, dy):
    right_side = window.width - paddle_sprite.width / 2
    left_side = paddle_sprite.width / 2

    if mouse_x > right_side:
        mouse_x = right_side
    if mouse_x < left_side:
        mouse_x = left_side

    paddle_sprite.x = mouse_x

def update_ball(dt):
    '''Update the ball's position based on its velocity.

    You can have docstrings on functions too.  Parameters are the
    variables that get passed in inside the parentheses.  A `float`
    is just a decimal number (eg. 5.3), as opposed to an `int`, which
    can only be an integer (eg. 5).

    :Parameters:
        `dt` : float
            The amount of time, in seconds, since the ball was last
            updated.
    '''
    # Delta means change, so `delta_pos` is the change in position of
    # the ball.  We multiply by `dt`, because we want the ball to
    # move by (50, -50) pixels every second, not every frame.
    delta_pos = ball_velocity * dt

    # Now we need to add the (x, y) components of our `delta_pos` to
    # the position of the sprite.
    ball_sprite.x = ball_sprite.x + delta_pos.x
    ball_sprite.y = ball_sprite.y + delta_pos.y

schedule_interval(update_ball, 1.0/60)


run()
