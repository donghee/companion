BASIC_AUTH_USER=admin
BASIC_AUTH_PASSWORD=admin
SERVER=http://192.168.88.97

AUTH=$(echo -ne "$BASIC_AUTH_USER:$BASIC_AUTH_PASSWORD" | base64 --wrap 0)

ACTION=zoomout

curl \
  --header "Content-Type: application/json" \
  --header "Authorization: Basic $AUTH" \
  --request GET \
  "$SERVER/web/cgi-bin/hi3510/ptzctrl.cgi?-step=0&-act=$ACTION&-speed=45"

sleep 1

curl \
  --header "Content-Type: application/json" \
  --header "Authorization: Basic $AUTH" \
  --request GET \
  "$SERVER/web/cgi-bin/hi3510/ptzctrl.cgi?-step=0&-act=stop&-speed=45"
