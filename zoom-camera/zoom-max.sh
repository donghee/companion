BASIC_AUTH_USER=admin
BASIC_AUTH_PASSWORD=admin
#CAMERA_IP=192.168.88.97
CAMERA_IP=192.168.10.101
SERVER=http://$CAMERA_IP

AUTH=$(echo -ne "$BASIC_AUTH_USER:$BASIC_AUTH_PASSWORD" | base64 --wrap 0)

ACTION=zoomin

curl \
  --header "Content-Type: application/json" \
  --header "Authorization: Basic $AUTH" \
  --request GET \
  "$SERVER/web/cgi-bin/hi3510/ptzctrl.cgi?-step=0&-act=$ACTION&-speed=45"

sleep 7

curl \
  --header "Content-Type: application/json" \
  --header "Authorization: Basic $AUTH" \
  --request GET \
  "$SERVER/web/cgi-bin/hi3510/ptzctrl.cgi?-step=0&-act=stop&-speed=45"
