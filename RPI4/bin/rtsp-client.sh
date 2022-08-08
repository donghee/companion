#!/bin/sh
STREAM_URL="rtsp://127.0.0.1:8554"
STREAM_KEY="test"

x=1
while [ $x -le 100000 ]
do
  echo "try connect to RTSP SERVER: $x times"

  # gstreamer rpicam
  #gst-launch-1.0 rpicamsrc keyframe-interval=2 bitrate=2500000 annotation-mode=custom-text+date+time annotation-text="UAV ID " annotation-mode=date+time preview=false vflip=false hflip=false ! video/x-h264,width=1280,height=720,framerate=15/1,profile=high ! h264parse ! rtspclientsink location=$STREAM_URL/$STREAM_KEY

  # RaspberryPi OS bullseye
  gst-launch-1.0 libcamerasrc ! video/x-raw,width=640,height=380,format=NV12,colorimetry=bt601,interlace-mode=progressive ! videoflip video-direction=identity ! clockoverlay time-format="%D %H:%M:%S" ! videorate ! video/x-raw,framerate=15/1 ! v4l2convert ! v4l2h264enc output-io-mode=2 extra-controls="controls,repeat_sequence_header=1,video_bitrate_mode=1,h264_profile=3,video_bitrate=1000000" ! video/x-h264,profile=main,level=\(string\)4 ! queue max-size-buffers=1 name=q_enc ! h264parse ! rtspclientsink location=$STREAM_URL/$STREAM_KEY

  x=$(( $x + 1 ))
  sleep 1
done
