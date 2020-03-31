## Overview

blinkt-persistence is a simple command line API, that allows manipulating Pimoroni Blinkt! lights by separate processes (original Python API allows for that only from a single process, since the device itself is write-only, and light states are just stored as global variable).

This API simply uses an internal cache to store the device state and restore it on every script execution. Not much efficient, but does the job. Contributions are welcome.

Using this API, user can write bigger programs, not necessarily in Python, that use Blinkt! LED lights as indicators of something, without digging into Blinkt! details.

## Usage

API v1 provides 2 simple scripts. The first, `set-pixel-rgb.py` allows setting a single "pixel" (LED light) into desired color and brightness:

`Usage: set-pixel-rgb.py <cache-file> <pixel:0-7> <brightness:0-10> <r:0-255> <g:0-255> <b:0-255>`

example:

`set-pixel-rgb.py /run/blinkt.json 0 7 0 200 0`

parameters:
- `cache-file` - rull path to JSON cache file (created if not exists, putting it inside `/run` directory will prevent surviving Raspberry Pi reboot)
- `pixel` - pixel number, from 0 (left side, near power port) to 7 (right side, near USB ports)
- `brightness` - either 0 (disabled but still set to given color) or 1-10
- `r`, `g`, `b` - RGB color components, 0-255

Another script, `set-brightness.py`, allows adjusting brightness of all lights at the same time:

`Usage: set-brightness.py <cache-file> <brightness:0-10>`

example:

`set-brightness.py /run/blinkt.json 1`

Setting brightness to 0 still preserves colors, so lights can be eg. turned off/on for a while (however original brightness is not preserved).

## Installing

First, you have to install Blinkt! software:

`curl https://get.pimoroni.com/blinkt | bash`

You can find more about Pimoroni Blinkt! devices [here](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt)

After thet, you can use this API.

## Compatibility

I've tested Pimoroni Blinkt! devices with Raspberry Pi 3B+ (rev. 1.3), and Raspberry Pi Zero, on Raspbian Jessie and Raspbian Stretch.

## License

|                      |                                          |
|:---------------------|:-----------------------------------------|
| **Author:**          | Tomasz Klim (<opensource@tomaszklim.pl>) |
| **Copyright:**       | Copyright 2018-2020 Tomasz Klim          |
| **License:**         | MIT                                      |

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
