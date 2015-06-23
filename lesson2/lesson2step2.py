'''Lesson 2 - step 2.

Handling collisions with the paddle.

TASKS:
    - Make the ball bounce off the paddle on collision.
    OR
    - Adapt this code to work with your own game.
'''

from pyglet.window import Window
from pyglet.image import load as load_image
from pyglet.sprite import Sprite
from pyglet.clock import schedule_interval
from pyglet.app import run

# `get_exit_direction` accepts two objects (object1, object2).  It
# then calculates the shortest distance to move `object1` out of
# `object2`, and returns a vector representing that movement.  If
# there is no collision, a vector (0, 0) will be returned.
from physics.collision import get_exit_direction
from physics.vector import Vector


window = Window()

paddle_image = load_image('paddle.png')
paddle_image.anchor_x = paddle_image.width / 2
paddle_sprite = Sprite(paddle_image, 0, 10)

ball_image = load_image('ball.png')
ball_sprite = Sprite(ball_image, 10, 300)
ball_velocity = Vector()
ball_velocity.x = 50
ball_velocity.y = -50

@window.event
def on_draw():
    window.clear()
    paddle_sprite.draw()
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
    '''Update the ball's position based on collisions and velocity.

    :Parameters:
        `dt` : float
            The amount of time, in seconds, since the ball was last
            updated.
    '''
    # You can continue long lines by wrapping statements in
    # parentheses.
    delta_pos = (ball_velocity * dt +
                 # It looks nicer when you indent in line with the
                 # opening parenthesis.
                 # We add the exit direction to the position of the
                 # ball to undo the collision.
                 get_exit_direction(ball_sprite, paddle_sprite))

    ball_sprite.x += delta_pos.x
    ball_sprite.y += delta_pos.y

schedule_interval(update_ball, 1.0/60)


run()
