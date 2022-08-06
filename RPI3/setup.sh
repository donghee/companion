mkdir ~/bin
cd ~/bin
# for raspberry pi arm7
wget https://github.com/aler9/rtsp-simple-server/releases/download/v0.19.3/rtsp-simple-server_v0.19.3_linux_armv7.tar.gz
tar xvfz rtsp-simple-server_v0.19.3_linux_armv7.tar.gz
chmod +x rtsp-simple-server

# gstreamer rpicamsrc
sudo apt-get install autoconf automake libtool pkg-config libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libraspberrypi-dev

cd ~/
git clone https://github.com/thaytan/gst-rpicamsrc
cd gst-rpicamsrc

./autogen.sh
make
sudo make install
