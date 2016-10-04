f = open("out.txt").read().split("\n")
out=""
for i in range(0,140821):
  #For each letter:
  nb = 0
  t = 0
  for l in f:
    t += 1
    letter = l[i*13:i*13+13]
    p = 0
    for c in letter:
      p+=1
      if c == "1":
        nb += 1*t*p
  out+=str(nb)+","


open('o2.txt','w').write( out)
