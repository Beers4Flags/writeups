#!/usr/bin/env python

import socket
import re

def answer(s, data="0\n"):
  s.send(data)
  s.recv(1000)

TCP_IP = 'misc.chal.csaw.io'
TCP_PORT = 8001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
text = s.recv(BUFFER_SIZE)
while 1:
  text1 = s.recv(BUFFER_SIZE)
  print text1
  i=0
  answer = ""
  last = ""
  while i < len(text1):
    c = text1[i]
    if c == "(":
      last = ""
      i += 1
      nextC = text1[i]
      add = 1
      while nextC != ")":
        if nextC == "|":
          add = 0
        if add == 1:
          last += nextC
        i += 1
        nextC = text1[i]
      answer += last
    elif c == "[":
      lastC = text1[i]
      i+=1
      nextC = text1[i]
      while nextC != "]":
        lastC = text1[i]
        last = lastC
        i+=1
        nextC = text1[i]
      answer += last
    elif c == "{":
      cnt = ""
      i += 1
      nextC = text1[i]
      while nextC != "}":
        nextC = text1[i]
        cnt += nextC
        i += 1 
      answer += last * (int(cnt[:-1])-1)
    elif c == "+":
      print "nothing"
    elif c == "*":
      print "nothing"
    elif c == "\\":
      i += 1
      nextC = text1[i] 
      if nextC == "d":
        last = "1"
      if nextC == "w":
        last = "a"
      answer += last
    else:
      last = c
      answer += last
  
    i = i+1
  print answer
  s.send(answer+"\n")  

  

s.close()

