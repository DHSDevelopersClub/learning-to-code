'''Lesson 2 - step 3.

Collisions with multiple objects.

TASKS:
    - 
    OR
    - Adapt this code to work with your own game.
'''

from pyglet.window import Window
from pyglet.image import load as load_image
from pyglet.sprite import Sprite
from pyglet.clock import schedule_interval
from pyglet.app import run

from physics.collision import get_exit_direction
from physics.vector import Vector
# `Rect` is short for rectangle.  A rect has `x`, `y`, `width`, and
# `height`, just like a Sprite.  However, a `Rect` is invisible.
from physics.rect import Rect


window = Window()

paddle_image = load_image('paddle.png')
paddle_image.anchor_x = paddle_image.width / 2
paddle_sprite = Sprite(paddle_image, 0, 10)

ball_image = load_image('ball.png')
ball_sprite = Sprite(ball_image, 10, 300)
# We can use `Vector.new(x, y)` to create a new vector directly with
# x and y values.
ball_velocity = Vector.new(50, -50)

# We create a `Rect` by calling `Rect.new` and passing in x, y, width,
# height.  Rects are nice for things that need to handle collisions.
top_wall = Rect.new(0, window.height, window.width, 0)

# You can make a list by wrapping a few objects in square brackets.
# `walls` is just a list of things that `ball_sprite` should collide
# with.
walls = [top_wall, paddle_sprite]

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
    # Set `delta_pos` to a blank vector.
    delta_pos = Vector()
    # A `for` loop allows us to loop through a list, and perform an
    # action on every item.  When we say `for wall in walls:`, we are
    # giving each item in the list `walls` the name of `wall`.  While
    # inside the `for` loop, we can refer to each wall as `wall`.
    for wall in walls:
        # For each wall, we add the exit direction from the wall to 
        # our total `delta_pos`.  The exit direction for most walls
        # will be <0, 0>, so it won't affect delta_pos.
        delta_pos += get_exit_direction(ball_sprite, wall)
    ball_velocity.copysign(delta_pos)
    delta_pos += ball_velocity * dt

    ball_sprite.x += delta_pos.x
    ball_sprite.y += delta_pos.y

schedule_interval(update_ball, 1.0/60)


run()
