#!/bin/bash

tmux new -d -s $USER
tmux new-window -n "raspberrypi"
tmux send-keys -t "$USER:raspberrypi" 'ssh pi@223.171.56.36' Enter
tmux new-window -n "mavproxy"
tmux send-keys -t "$USER:mavproxy" 'mavproxy.py --master=tcp:223.171.56.36:5760 --master=tcp:192.168.100.101:5760 --out=udp:0.0.0.0:14550 --console --map --load-module=horizon' Enter
tmux new-window -n "joystick"
tmux send-keys -t "$USER:joystick" 'cd scripts && sudo chmod 666 /dev/uinput && python3 virtual-joy.py' Enter
tmux new-window -n "streaming"
tmux send-keys -t "$USER:streaming" 'cd rtsp-server; ./run.sh' Enter
tmux new-window -n "detect"
tmux send-keys -t "$USER:detect" 'cd object-detect; ./run.sh' 
