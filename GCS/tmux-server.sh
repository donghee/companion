#!/bin/bash

tmux new -d -s $USER
tmux new-window -n "mavproxy"
tmux send-keys -t "$USER:mavproxy" 'mavproxy.py --master=tcp:223.171.56.36:5760 --master=/dev/ttyUSB0 --out=udp:0.0.0.0:14550 --console --map --load-module=horizon' Enter
tmux new-window -n "joystick"
tmux send-keys -t "$USER:joystick" 'cd scripts; python3 virtual-joy.py' Enter
tmux new-window -n "streaming"
tmux send-keys -t "$USER:streaming" 'cd rtsp-server; ./run.sh' Enter
tmux new-window -n "detect"
tmux send-keys -t "$USER:detect" 'cd object-detect; ./run.sh' Enter
