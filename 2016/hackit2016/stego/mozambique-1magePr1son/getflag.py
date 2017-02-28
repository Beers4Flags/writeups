#! /usr/local/bin/python
#-*- coding: utf-8 -*-

from PIL import Image
import string


chall = Image.open("planet.png")
l,h = chall.size
pix_chall = chall.load()
red = ""
blue= ""
green = ""
buffer = ""
img = Image.new( 'RGB', (63,63))
outpix = img.load()

i = 0
j = 0
for y in range(0,h, 24):
	for x in range(0,l,24):
		print i, j
		r,g,b = pix_chall[x,y]
		try:
			outpix[i,j] = (r, g, b)
		except:
			print ""
		i = i +1
	j = j + 1
	i = 0
img.save('outgrid.png')
