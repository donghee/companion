RSSI=`curl -vs -u admin:1234admin# --cookie "language=en" http://192.168.10.254/adm/status.asp?model=cnr-l500w  2>&1 | sed -n "s/.*RSSI.*<td>\(.*\)<\/td>.*/\1/p"`
SINR=`curl -vs -u admin:1234admin# --cookie "language=en" http://192.168.10.254/adm/status.asp?model=cnr-l500w  2>&1 | sed -n "s/.*SINR.*<td>\(.*\)<\/td>.*/\1/p"`
PROVIDER=`curl -vs -u admin:1234admin# --cookie "language=en" http://192.168.10.254/adm/status.asp?model=cnr-l500w  2>&1 | sed -n "s/.*Provider.*<td>\(.*\)<\/td>.*/\1/p"`

#4 grades: > -65 (excellent signal)
#3 grades: from -65 to -75 (good signal)
#2 grades: from -75 to -85 (medium signal)
#1 grade: from -85 to -90 (poor signal)
#0 grade: < -90 (no connection)

while true; do 
	echo -e "{\"rssi\": \"$RSSI dBm\", \"sinr\": \"$SINR dB\", \"provider\": \"$PROVIDER\", \"date\": \"$(date)\"}" > /tmp/index.html
   sleep 30; 
done
