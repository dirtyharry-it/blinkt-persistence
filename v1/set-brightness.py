#!/usr/bin/env python
#
'''
## License

The MIT License (MIT)

Copyright (c) 2018-2021 Tomasz Klim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys
import blinkt
import json
import time
import random
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
    if os.path.getsize(fname) == 0:
        time.sleep(random.uniform(0.07,0.22))
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
