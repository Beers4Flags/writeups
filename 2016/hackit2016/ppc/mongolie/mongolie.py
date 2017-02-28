#!/usr/bin/env python

import httplib
import re
import urllib2
import urllib
import base64
import cookielib
import sys

import socket
from time import sleep

def answer(s, data="0\n"):
  s.send(data)

cookies = cookielib.LWPCookieJar()
handlers = [
    urllib2.HTTPHandler(),
    urllib2.HTTPSHandler(),
    urllib2.HTTPCookieProcessor(cookies)
    ]
opener = urllib2.build_opener(*handlers)

def fetch(uri):
    req = urllib2.Request(uri)
    return opener.open(req)

def post(uri, data):
    req = urllib2.Request(uri, data)
    req.get_method = lambda: 'POST'
    req.add_header("Content-type", "application/x-www-form-urlencoded")
    return opener.open(req)

def dump():
    for cookie in cookies:
        print cookie.name, cookie.value

uri = "http://factordb.com/index.php?query="

TCP_IP = 'ctf.com.ua'
TCP_PORT = 9988
BUFFER_SIZE = 4096
INIT_SIZE = 500 - 330 -4

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
text = s.recv(INIT_SIZE)
print text
for j in range (0,100):
  sleep(1)
  tr = s.recv(BUFFER_SIZE)
  print tr
  print j
  t = re.search('\d+', tr)
  text = t.group(0)
  #print text
  res = fetch(uri+text)
  res = res.read()
  m = re.search('<font color="\#002099">(\d+)<\/font><\/a>\)\^(\d+) =', res) 
  print m.group(1)
  print m.group(2)
    
  answer(s, m.group(1)+" " + m.group(2)+"\n")

print s.recv(1024)

s.close()

