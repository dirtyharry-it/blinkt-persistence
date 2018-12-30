#!/usr/bin/env python

import sys
import blinkt
import json
import os.path


def usage():
    print("Usage: {} <cache-file> <brightness:0-10>".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 3:
    usage()

try:
    brightness = int(sys.argv[2])
except ValueError:
    usage()


# either read the cache file or initialize cache with all pixels off
fname = sys.argv[1]
if os.path.isfile(fname):
    with open(fname) as f:
        pixels = json.load(f)
else:
    pixels = [[0, 0, 0, blinkt.BRIGHTNESS]] * blinkt.NUM_PIXELS

# restore pixel states from cache file, but adjust brightness
for x in range(blinkt.NUM_PIXELS):
    pixels[x][3] = brightness
    blinkt.set_pixel(x, pixels[x][0], pixels[x][1], pixels[x][2], pixels[x][3] / 10.0)

# push the changed pixel to Blinkt! device
blinkt.set_clear_on_exit(False)
blinkt.show()

# save the cache to file
with open(fname, 'w') as outfile:
    json.dump(pixels, outfile)
