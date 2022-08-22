# Virtual Joystick

sudo apt-get install python3-evdev

sudo apt update && sudo apt dist-upgrade -y

sudo apt install -y libudev-dev libusb-1.0-0-dev libhidapi-libusb0
sudo apt install -y libjpeg-dev zlib1g-dev libopenjp2-7 libtiff5

# Install python library dependencies
pip3 install wheel
pip3 install pillow

# Add udev rule to allow all users non-root access to Elgato StreamDeck devices:
sudo tee /etc/udev/rules.d/10-streamdeck.rules << EOF
    SUBSYSTEMS=="usb", ATTRS{idVendor}=="0fd9", GROUP="users", TAG+="uaccess"
EOF

sudo udevadm control --reload-rules

pip3 install streamdeck

# MAVProxy console 

sudo apt-get install python3-dev python3-opencv python3-wxgtk4.0 python3-pip python3-matplotlib python3-lxml python3-pygame

# SITL

docker run -it --rm -p 5760:5760   -v `pwd`:/ardupilot ardupilot:latest bash
sudo pip3 install mavproxy
sim_vehicle.py -v ArduCopter --no-mavproxy
