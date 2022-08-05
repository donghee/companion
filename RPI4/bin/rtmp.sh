#!/bin/bash
STREAM_URL="dev.dronemap.io/live"
STREAM_KEY="donghee"

x=1
while [ $x -le 100000 ]
do
  echo "try connect to RTMP SERVER: $x times"

  # gstreamer
  gst-launch-1.0 rpicamsrc keyframe-interval=2 bitrate=2500000 annotation-mode=date+time preview=false ! video/x-h264,width=1280,height=720,framerate=15/1,profile=high ! h264parse ! flvmux ! rtmpsink location='rtmp://live.dronemap.io/live/donghee live=1'

  # rspivid + rtmp
  #raspivid -o - -t 0 -w 1280 -h 720 -ev 25 -ex nightpreview -fps 25 -b 6000000 | ffmpeg -f h264 -i - -vcodec copy -c:a aac -f flv rtmp://$STREAM_URL/$STREAM_KEY

  x=$(( $x + 1 ))
  sleep 1
done
