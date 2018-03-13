#!/usr/bin/env python

import sys
import os
import array

def reverse_processing(byte):
	res = byte | 0x80
	res = res ^ 0xCA
	res = res + 66
	res = res ^ 0xCA
	res = res + 66
	res = res ^ 0xCA
	res = res + 66
	res = res ^ 0xFE

	return res

expected = open('expected.bin', 'rb').read()
flag = []
for i, e in enumerate(expected):
	for i in range(ord(' '), ord('~')):
		res = reverse_processing(i)
		if res & 0xff == e:
			flag.append(chr(i))
			break

# Reverse characters
flag = array.array('u', flag)
for i in range(0, len(flag)//2):
	tmp = flag[i]
	flag[i] = flag[len(flag)-i-1]
	flag[len(flag)-i-1] = tmp

print('flag: ' + ''.join(flag))
