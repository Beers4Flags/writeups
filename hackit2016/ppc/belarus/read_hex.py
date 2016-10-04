def h2s(text):
  answer = ""
  for i in range(0, len(text), 2):
    answer += str(chr(int(text[i]+text[i+1], 16)))
  return answer

data = open("o2.txt").read()

open("jfif.file",'w').write( h2s(data))
