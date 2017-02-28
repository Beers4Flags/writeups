**No Humans Allowed- 200pts**

For this chall, you have a calcul to do.

A simple curl on website :

```BASH
<docType 5="5"></docType><html lang="en"><head><link rel="stylesheet" href="/pub/styles/site.css"/><title>Robot Liberation</title></head><body><div id="div" class="banner">Robot Liberation!</div><div id="div" class="content"><h2>Prove you are a robot.</h2><p>Provide the answer. You have 1000 miliseconds.</p><p>60452 + 27816</p><form method="post"><input type="text" name="val3"/><input type="submit" value="Send Answer"/></form></div></body></html>
```

So you just have to do regex/split, this is the script I made :

```python
#!/usr/bin/env python

import requests
import urllib2
import urllib

url = 'http://neverlanctf-challenges-elb-248020705.us-west-2.elb.amazonaws.com:9129/'

while True:
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	cookies=response.info()['Set-Cookie']
	content = response.read()
	print content
	print ""
	content2 = content.split('+')
	n1 = content2[0].split('<p>')
	n1 = n1[-1]
	n2 = content2[1].split('</p>')
	n1 = n2[0]
	n1 = n2.replace(' ','')

	print n1
	print n2
	res = int(n1) + int(n2)
	print res

	data = {}
	data['val3'] = str(res)
	url_values = urllib.urlencode(data)
	full_url = url + '?' + url_values
	req = urllib2.Request(full_url)
	req.add_header("Cookie", cookies)
	#response = urllib2.urlopen(req)
	response = urllib2.urlopen(req, url_values)
	content = response.read()
	print content
```


The result :

```BASH
36328 
41174
77502
<docType 5="5"></docType><html lang="en"><head><link rel="stylesheet" href="/pub/styles/site.css"/><title>Robot Liberation</title></head><body><div id="div" class="banner">Robot Liberation!</div><div id="div" class="content"><h2>Robot Detected</h2><p>Your key: jHBhbfoY1UEHQuRMwzt7Yr8xkCiCvfbS</p></div></body></html>
<docType 5="5"></docType><html lang="en"><head><link rel="stylesheet" href="/pub/styles/site.css"/><title>Robot Liberation</title></head><body><div id="div" class="banner">Robot Liberation!</div><div id="div" class="content"><h2>Prove you are a robot.</h2><p>Provide the answer. You have 1000 miliseconds.</p><p>15701 + 94307</p><form method="post"><input type="text" name="val3"/><input type="submit" value="Send Answer"/></form></div></body></html>
```

We can see :  Robot Detected</h2><p>Your key: jHBhbfoY1UEHQuRMwzt7Yr8xkCiCvfbS

The flag is : jHBhbfoY1UEHQuRMwzt7Yr8xkCiCvfbS


By team Beers4Flags

```
 ________
|        |
|  #BFF  |
|________|
   _.._,_|,_
  (      |   )
   ]~,"-.-~~[
 .=] Beers ([
 | ])  4   ([
 '=]) Flags [
   |:: '    |
    ~~----~~
```
