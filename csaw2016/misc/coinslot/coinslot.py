#!/usr/bin/env python

import socket
import re

def answer(s, data="0\n"):
  s.send(data)
  s.recv(1000)

TCP_IP = 'misc.chal.csaw.io'
TCP_PORT = 8000
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
for j in range (0,2016):
  text = s.recv(BUFFER_SIZE)
  print str(j)+ ":"+text
  match = re.search('(\d+)\.(\d\d)', text)
  s1 = match.group(0)
  print str(j)+" "+s1
  sum = round(float(s1)*100)
  left = int(sum)
  i1 = int(left / 1000000 )
  left = left - i1 * 1000000
  i2 = int(left/ 500000) 
  left = left - i2 * 500000
  i3 = int(left / 100000) 
  left = left - i3 * 100000
  i4 = int(left / 50000) 
  left = left - i4 * 50000
  i5 = int(left / 10000) 
  left = left - i5 * 10000
  i6 = int(left / 5000) 
  left = left - i6 * 5000
  i7 = int(left / 2000) 
  left = left - i7 * 2000
  i8 = int(left / 1000) 
  left = left - i8 * 1000
  i9 = int(left / 500) 
  left = left - i9 * 500
  i10 = int(left / 100) 
  left = left - i10 * 100
  i11 = int(left / 50) 
  left = left - (i11 * 50)
  i12 = int(left / 25) 
  left = left - (i12 * 25)
  i13 = int(left / 10) 
  left = left - (i13 *10)
  i14 = int(left / 5) 
  left = left - i14 * 5
  i15 = int(left / 1) 
  left = left - i15 * 1
  answer(s, str(i1)+"\n")
  answer(s, str(i2)+"\n")
  answer(s, str(i3)+"\n")
  answer(s, str(i4)+"\n")
  answer(s, str(i5)+"\n")
  answer(s, str(i6)+"\n")
  answer(s, str(i7)+"\n")
  answer(s, str(i8)+"\n")
  answer(s, str(i9)+"\n")
  answer(s, str(i10)+"\n")
  answer(s, str(i11)+"\n")
  answer(s, str(i12)+"\n")
  answer(s, str(i13)+"\n")
  answer(s, str(i14)+"\n")
  s.send(str(i15)+"\n")

print s.recv(1024)

s.close()

