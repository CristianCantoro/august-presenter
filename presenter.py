#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""August Presenter.

Usage:
  presenter.py [-v]
  presenter.py [-v] (-d NAME | --device=NAME)
  presenter.py (-h | --help)
  presenter.py --version

Options:
  -d NAME,--device=NAME Device NAME
                        [default: /dev/input/by-id/usb-1d57_ad03-event-kbd].
  -v                    Verbose output
  -h, --help             Show this screen.
  --version             Show version.
"""

from evdev import InputDevice
from evdev import categorize
from evdev import ecodes
from subprocess import call
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='August Presenter 0.1')

    verbose = arguments['-v']

    device = arguments['--device']

    # This is already taken care of by docopt
    # if device is None:
    #     device = '/dev/input/by-id/usb-1d57_ad03-event-kbd'

    dev = InputDevice(device)
    print(dev)

    dev.capabilities()

    screenLocked = False
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            if verbose:
                print(categorize(event))

            if event.code == ecodes.KEY_B and event.value == 1:
                if not screenLocked:
                    call(["xset", "dpms", "force", "off"])
                    screenLocked = True
                else:
                    screenLocked = False
