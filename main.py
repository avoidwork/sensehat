#!/usr/bin/python

import time
from sense_hat import SenseHat

s = SenseHat()
s.low_light = True
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)
colors = [nothing, green, yellow, red]
max = len(colors) - 1
current = 1
prev = 0
off = 0


def init():
    W = white
    B = blue
    O = nothing
    logo = (
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        W, W, W, B, O, O, O, B,
        W, O, W, B, O, O, O, B,
        W, W, W, B, O, B, O, B,
        W, O, W, O, B, O, B, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
    )
    return logo


def color(pos=0):
    global current

    if pos > 0:
        global prev
        prev = current

    current = pos
    return colors[current] * 64


try:
    s.set_pixels(init())
    time.sleep(1)
    s.set_pixels(color(1))

    while True:
        for event in s.stick.get_events():
            if event.action == 'released':
                if event.direction == 'middle':
                    off ^= 1
                    s.set_pixels(color(0 if off == 1 else prev))
                elif off == 0:
                    current = current + 1 if event.direction == 'up' else current - 1
                    current = max if current < 1 else 1 if current > max else current
                    s.set_pixels(color(current))

except KeyboardInterrupt:
    s.set_pixels(color(0))
