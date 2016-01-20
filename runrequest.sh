# return "msg":"bad signature" for now
# can not work

currentutctimestamp=`date -d now +%s`
randomnumber0=`head -200 /dev/urandom | cksum | cut -c -8`
randomnumber=`cat /proc/sys/kernel/random/uuid | cut -c 3,6,12,16,23,26,30,34`
echo " "
baseurl="https://openapi.kuaipan.cn/open/requestToken"
consumerkey="bc3DFCVFddQXJcON"  # fake consumerkey
consumersecret="z33pLA2ICWf5paV0"
signature=""
hmackey="z33pLA2ICWf5paV0&"  # fake hmackey

equalsign=`echo "=" | ./urlencode4sh.sh`
andsign=`echo "&" | ./urlencode4sh.sh`
baseurlencode=`echo $baseurl | ./urlencode4sh.sh`

urlstrencode="GET&"$baseurlencode"&""oauth_comsumer_key"$equalsign$consumerkey$andsign"oauth_nonce"$equalsign$randomnumber$andsign"oauth_signature_method"$equalsign"HMAC-SHA1"$andsign"oauth_timestamp"$equalsign$currentutctimestamp$andsign"oauth_version"$equalsign"1.0"
echo $urlstrencode
echo " "
sigtrestr=`echo -n $urlstrencode | openssl dgst -sha1 -hmac \"$hmackey\" -binary | base64 | ./urlencode4sh.sh`
echo $sigtrestr
echo " "

urlstr=$baseurl"?oauth_signature="$sigtrestr"&oauth_consumer_key="$consumerkey"&oauth_nonce="$randomnumber"&oauth_signature_method=HMAC-SHA1&oauth_timestamp="$currentutctimestamp"&oauth_version=1.0"

echo $urlstr
echo " "
#curl -k $aa
echo " "
