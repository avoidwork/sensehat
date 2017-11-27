#!/usr/bin/python

import sys
import time
from random import randint
from sense_hat import SenseHat

s = SenseHat()
s.low_light = True
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
colors = [nothing, green, yellow, red]
max = len(colors) - 1
current = 1
prev = 0
off = 0

def grid_init():
    W = white
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    W, W, W, B, O, O, O, B,
    W, O, W, B, O, O, O, B,
    W, W, W, B, O, B, O, B,
    W, O, W, B, B, O, B, B,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def grid_draw(fill):
    s.set_pixels(fill)

def grid_color(pos=0):
    global current

    if pos > 0:
        global prev
        prev = current

    current = pos
    return [[colors[current]]*64][0]

def grid_clear():
    grid_draw(grid_color(0))

try:
    grid_draw(grid_init())
    time.sleep(1)
    grid_draw(grid_color(1))

    while True:
        for event in s.stick.get_events():
            if event.action == 'released':
                if event.direction == 'middle':
                    off ^= 1
                    grid_draw(grid_color(0 if off == 1 else prev))
                elif off == 0:
                    current = current + 1 if event.direction == 'up' else current - 1
                    current = max if current < 1 else 1 if current > max else current
                    grid_draw(grid_color(current))

except KeyboardInterrupt:
    grid_clear()
