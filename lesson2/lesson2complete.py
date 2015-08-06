'''Lesson 2 - complete.

Example of a completed lesson 2.
'''

from pyglet.window import Window
from pyglet.image import load as load_image
from pyglet.sprite import Sprite
from pyglet.clock import schedule_interval
from pyglet.app import run

from physics.collision import get_exit_direction
from physics.vector import Vector
from physics.rect import Rect


window = Window()

paddle_image = load_image('paddle.png')
paddle_sprite = Sprite(paddle_image, 0, 10)

ball_image = load_image('ball.png')
ball_sprite = Sprite(ball_image, 10, 300)
ball_velocity = Vector.new(50, -50)

left_wall = Rect.new(0, 0, 0, window.height)
top_wall = Rect.new(0, window.height, window.width, 0)
right_wall = Rect.new(window.width, 0, 0, window.height)

walls = [left_wall, top_wall, right_wall, paddle_sprite]

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

    paddle_sprite.x = mouse_x - paddle_sprite.width / 2

def update_ball(dt):
    delta_pos = Vector()
    for wall in walls:
        delta_pos += get_exit_direction(ball_sprite, wall)
    ball_velocity.copysign(delta_pos)
    delta_pos += ball_velocity * dt

    ball_sprite.x += delta_pos.x
    ball_sprite.y += delta_pos.y

schedule_interval(update_ball, 1.0/60)


run()
