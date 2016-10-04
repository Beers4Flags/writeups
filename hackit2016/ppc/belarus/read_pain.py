from collections import Counter
lines = open("orig.txt").read().split("\n")[:-1]
out = ""
for line in lines:
  i=0
  while i < len(line):
    if ord(line[i]) == 226:
      out +="1"
      i+=3 # This means it's a 1
    else:
      i+=1
      out+=" "
  out+="\n"

open("out.txt",'w').write( out )
