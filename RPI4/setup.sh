sudo apt-get install python3-dev python3-opencv python3-wxgtk4.0 python3-pip python3-matplotlib python-pygame python3-lxml libxml2-dev libxslt-dev tmux git -y
pip3 install PyYAML pyserial mavproxy --user

sudo adduser $USER dialout
echo "%$USER ALL=NOPASSWD: ALL" | sudo tee -a /etc/sudoers

sudo apt-get install gstreamer-1.0 \
    libgstreamer-plugins-base1.0-dev \
    libgstrtspserver-1.0-dev -y

sudo cp services/*.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable rtsp-client
sudo systemctl enable rtsp-simple-server
#sudo systemctl enable telem-proxy
sudo systemctl enable tmux-server

mkdir ~/bin
cd ~/bin
wget https://github.com/aler9/rtsp-simple-server/releases/download/v0.19.3/rtsp-simple-server_v0.19.3_linux_arm64v8.tar.gz
tar xvfz rtsp-simple-server_v0.19.3_linux_arm64v8.tar.gz
chmod +x rtsp-simple-server

# ttyd
wget https://github.com/tsl0922/ttyd/releases/download/1.6.3/ttyd.arm
chmod +x ttyd.arm

cd ~/
