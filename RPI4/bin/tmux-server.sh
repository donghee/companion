#!/bin/bash

tmux new -d -s $USER -n "mavproxy"
#tmux send-keys -t "$USER:mavproxy" 'cd ~; ./mavproxy.sh' Enter
tmux new-window -n "frp"
tmux send-keys -t "$USER:frp" 'cd ~; ./frpc.sh' Enter
tmux new-window -n "streaming"
#tmux send-keys -t "$USER:streaming" 'cd ~; ./rtsp.sh' Enter
#tmux send-keys -t "$USER:streaming" 'cd ~; ./rtmp.sh' Enter
tmux send-keys -t "$USER:streaming" 'cd ~/bin; ./rtsp-client.sh' Enter
tmux new-window -n "ttyd"
tmux send-keys -t "$USER:ttyd" 'cd ~/bin; ./ttyd.arm -p 8080 -P 1 bash' Enter
tmux new-window -n "ttyd-nsh"
tmux send-keys -t "$USER:ttyd-nsh" 'cd ~/bin; ./ttyd.arm -p 8081 tmux attach -t pi:nsh' Enter
tmux new-window -n "ttyd-dim"
tmux send-keys -t "$USER:ttyd-dim" 'cd ~/bin; ./ttyd.arm -p 8082 tmux attach -t pi:dim' Enter
tmux new-window -n "dim"
tmux send-keys -t "$USER:dim" 'cd ~/mavlink-dim; ./server.sh' Enter
tmux new-window -n "status"
tmux send-keys -t "$USER:status" 'cd ~/bin && (./lte-status.sh &) && ./run-lte-status.sh' Enter
tmux new-window -n "nsh"
tmux send-keys -t "$USER:nsh" 'cd ~; picocom /dev/ttyUSB0 -b 57600'
