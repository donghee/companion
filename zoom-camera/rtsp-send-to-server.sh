ffmpeg -i rtsp://192.168.10.101:554/2  -pix_fmt yuv420p -preset ultrafast -b:v 600k -f rtsp rtsp://localhost:8554/zoom
