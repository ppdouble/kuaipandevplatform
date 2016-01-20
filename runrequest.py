# works fine
# nick.d.dong(at)gmail.com

import time
import random
import string
from urllib import quote
import base64
import hmac
import urllib2
import hashlib
import urllib

currentutctimestamp = str(time.time()).split('.')[0]
randomstr = ''.join(random.sample(string.ascii_letters + string.digits, 8))

baseurl="https://openapi.kuaipan.cn/open/requestToken"
consumerkey="bc3DFCVFddQXJcON"  # fake consumerkey
signature=""
hmackey="z33pLA2ICWf5paV0&"  # fake hmackey
http_method = "GET"
equalsign = quote("=")
andsign = quote("&")
baseurldict = {
        'burl': 'https://openapi.kuaipan.cn/open/requestToken'
}
parameters = {
        'oauth_consumer_key': consumerkey,
        'oauth_nonce': randomstr,
        'oauth_signature_method' : 'HMAC-SHA1',
        'oauth_timestamp' : currentutctimestamp,
        'oauth_version': '1.0'
}
urlencode = urllib.urlencode(baseurldict).split('=')[1]  + "&" + \
quote("&".join(sorted([quote ( k ) + "=" + quote ( v ) for k, v in parameters.items()])))

urlstrencode = http_method + "&" + urlencode
print urlstrencode
signaturetoencode = hmac.new(hmackey,urlstrencode,hashlib.sha1).digest().encode('base64').rstrip()
signature = urllib.urlencode({'sgtstr': signaturetoencode}).split('=')[1]
print signature

urlstr = baseurl + "?" + "oauth_signature=" + signature + "&oauth_consumer_key=" + consumerkey+ "&oauth_nonce=" + randomstr + "&oauth_signature_method=HMAC-SHA1" + "&oauth_timestamp=" + currentutctimestamp + "&oauth_version=1.0"

print urlstr

rf = urllib2.urlopen(urlstr)
buf = rf.read()
rf.close()
print buf
