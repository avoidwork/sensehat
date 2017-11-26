from sense_hat import SenseHat
from random import randint
import time
import sys

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
colors = [nothing, blue, yellow, red]
current = 0

def grid_init():
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    Y, Y, Y, B, O, O, O, B,
    Y, O, Y, B, O, O, O, B,
    Y, Y, Y, B, O, B, O, B,
    Y, O, Y, B, B, O, B, B,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def grid_draw(fill):
    s.set_pixels(fill)

def grid_color(pos=0):
    current = pos
    fill = [[colors[current]]*64][0]
    return fill

def grid_clear():
    grid_draw(grid_color(0))

try:
    grid_draw(grid_init())
    time.sleep(1)
    grid_draw(grid_color(1))

    while True:
        for event in s.stick.get_events():
            if event.action == 'released':
                current = current + 1 if event.direction == 'up' else current - 1

                if current < 0:
                    current = len(colors)
                elif current > len(colors):
                    current = 0

                grid_draw(grid_color(current))

except KeyboardInterrupt:
    grid_clear()
