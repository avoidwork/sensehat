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

def grid_color(score=0):
    c = red if score > 75 else yellow if score > 50 else blue if score > 25 else nothing
    return [[c]*64][0]

def grid_clear():
    s.set_pixels(grid_color(0))

try:
    s.set_pixels(grid_init())
    time.sleep(.75)

    while True:
        s.set_pixels(grid_color(randint(26, 100)))
        time.sleep(.75)

except KeyboardInterrupt:
    grid_clear()
