#!/usr/bin/env python

import sys
import blinkt
import json
import time
import random
import os.path


def usage():
    print("Usage: {} <cache-file> <pixel:0-7> <brightness:0-10> <r:0-255> <g:0-255> <b:0-255>".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 7:
    usage()

try:
    pixel, brightness, r, g, b = [int(x) for x in sys.argv[2:]]
except ValueError:
    usage()

if max(r, g, b) > 255:
    usage()

if pixel > 7:
    usage()


# either read the cache file or initialize cache with all pixels off
fname = sys.argv[1]
if os.path.isfile(fname):
    if os.path.getsize(fname) == 0:
        time.sleep(random.uniform(0.07,0.22))
    with open(fname) as f:
        pixels = json.load(f)
else:
    pixels = [[0, 0, 0, blinkt.BRIGHTNESS]] * blinkt.NUM_PIXELS

# restore pixel states from cache file
for x in range(blinkt.NUM_PIXELS):
    blinkt.set_pixel(x, pixels[x][0], pixels[x][1], pixels[x][2], pixels[x][3] / 10.0)

# push the changed pixel to Blinkt! device
blinkt.set_clear_on_exit(False)
blinkt.set_pixel(pixel, r, g, b, brightness / 10.0)
blinkt.show()

# push the changed pixel to cache and save it
pixels[pixel] = [r & 0xff, g & 0xff, b & 0xff, brightness]
with open(fname, 'w') as outfile:
    json.dump(pixels, outfile)
