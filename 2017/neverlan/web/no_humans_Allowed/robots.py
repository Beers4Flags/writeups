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
	url="http://neverlanctf-challenges-elb-248020705.us-west-2.elb.amazonaws.com:9129/"
	url_values = urllib.urlencode(data)
	full_url = url + '?' + url_values
	req = urllib2.Request(full_url)
	req.add_header("Cookie", cookies)
	#response = urllib2.urlopen(req)
	response = urllib2.urlopen(req, url_values)
	content = response.read()
	print content
