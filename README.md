# august-presenter
A small python script to switch blank screen on and off with an August wireless
presenter (model no.: [LP205R](http://www.amazon.co.uk/August-LP205R-Wireless-Presenter-Pointer/dp/B004B3V5PQ))

This script maps the input of the blank screen button - equal to pressing
the key `b` - to the command `xset dpms force off` which on Linux blanks the
screen.

## Requirements
This script requires the modules `evdev` and `docopt`

## Usage
You should run this command with `sudo` (which is needed to access the input
device).

```
$ sudo ./presenter.py
```

### Options
```
$ ./presenter.py -h
August Presenter.

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
```