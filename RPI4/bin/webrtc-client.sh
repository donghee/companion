#!/bin/sh

# Send camera stream to janus webrtc videoroom 
x=1
while [ $x -le 100000 ]
do
  echo "try connect to WEBRTC SERVER: $x times"

curl -H 'Content-Type: application/json' -d '{"id": "abc123", "room": 1234, "token": "verysecret"}' https://whip.rtc.baribarilab.com/whip/create

./whip-client -u https://whip.rtc.baribarilab.com/whip/endpoint/abc123 \
-t verysecret \
-V "rpicamsrc preview=false ! video/x-raw, width=1920, height=1080, framerate=15/1 ! clockoverlay font-desc=\"Arial 40px\" ! videoconvert ! v4l2h264enc extra-controls=\"controls, h264_profile=4, video_bitrate=3000000\" ! video/x-h264,level=(string)4 ! h264parse ! rtph264pay config-interval=1 ! application/x-rtp,media=video,encoding-name=H264,payload=96"

# v4l2h264enc hardware encoder
# level: https://en.wikipedia.org/wiki/Advanced_Video_Coding#Levels
#-V "rpicamsrc preview=false ! video/x-raw, width=1280, height=720, framerate=15/1 ! clockoverlay font-desc=\"Arial 40px\" ! videoconvert ! v4l2h264enc extra-controls=\"controls, h264_profile=4, video_bitrate=620000\" ! video/x-h264,level=(string)4 ! h264parse ! rtph264pay config-interval=1 ! application/x-rtp,media=video,encoding-name=H264,payload=96"
#-V "rpicamsrc preview=false ! video/x-raw, width=1920, height=1080, framerate=15/1 ! clockoverlay font-desc=\"Arial 40px\" ! videoconvert ! v4l2h264enc extra-controls=\"controls, h264_profile=4, video_bitrate=620000\" ! video/x-h264,level=(string)4 ! h264parse ! rtph264pay config-interval=1 ! application/x-rtp,media=video,encoding-name=H264,payload=96"
# x264enc software encoder
#-V "rpicamsrc preview=false ! video/x-raw, width=1280, height=720, framerate=15/1 ! clockoverlay font-desc=\"Arial 40px\" ! videoconvert ! x264enc ! rtph264pay config-interval=1 ! application/x-rtp,media=video,encoding-name=H264,payload=96"

curl -X DELETE -H "Authorization: Bearer verysecret" https://whip.rtc.baribarilab.com/whip/endpoint/abc123

  x=$(( $x + 1 ))
  sleep 1
done
