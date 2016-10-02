#!/usr/bin/env python

import sys
import cv2

#./h4ck1t_pepapig.py 468 rgb

def recompose(lsb_str, byte_len):
    byte_lst = []
    nwstr = "".join([ chr(int(lsb_str[i:i+byte_len],2)) for i in range(0,len(lsb_str),byte_len) ])
    return str(nwstr)


def compare(maxpx, ch):
    im0 = cv2.imread("vidz.png")
    im1 = cv2.imread("vidz-orig.png")
    line, col, band = im0.shape
    bit_str = ""
    for x in range(0, line):
        for y in range(0,col):
            for z in ch:
                if x*y < maxpx:
                    print "Original ("+str(x)+" "+str(y)+" "+str(z)+") => "+str(im1[x,y,z])
                    print "Modified ("+str(x)+" "+str(y)+" "+str(z)+") => "+str(im0[x,y,z])
                    bit_str += str( im1[x,y,z] - im0[x,y,z])
                else:
                    return bit_str

maxpx = int(sys.argv[1])
chan = { 'r' : 2, 'g' : 1, 'b' : 0, 'a' : 3 }
ch = [ chan[sys.argv[2][i]] for i in range(0,len(sys.argv[2]))]
bit_str = compare(maxpx, ch)
print recompose(bit_str,8)
