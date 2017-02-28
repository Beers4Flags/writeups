#!/usr/python

import requests
import re

p = re.compile(ur'IceCTF\{.*\}')

urls = ["https://icec.tf", "https://icec.tf/about", "https://icec.tf/faq", "https://icec.tf/contact", "https://icec.tf/sponsors"]

for url in urls:
	r = requests.get(url)
	res = re.search(p, r.text)
	if res:
		print "Flag found in "+url+"==>"+res.group(0)
	else:
		print "No flag in "+url
