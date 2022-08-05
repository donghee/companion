#!/bin/sh

QGC_IP='192.168.88.250'
x=1
while [ $x -le 100 ]
do
  echo "try connect to GCS: $x times"
  gst-launch-1.0 rpicamsrc bitrate=2000000 ! 'video/x-h264,width=720,height=480' ! h264parse ! queue ! rtph264pay config-interval=1 pt=96 ! udpsink host=$QGC_IP port=5600

  x=$(( $x + 1 ))
  sleep 1
done
