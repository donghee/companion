#!/bin/bash

BAUD_RATE=921600
TELEM_PORT=/dev/ttyS0

/usr/bin/python3 $HOME/.local/bin/mavproxy.py --master=/dev/ttyS0 --baudrate $BAUD_RATE --out=tcpin:0.0.0.0:5760 --daemon
