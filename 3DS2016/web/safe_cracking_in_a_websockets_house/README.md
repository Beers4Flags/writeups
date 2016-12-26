#Safe Cracking in a Websocket's House

 Your mission is:
1. Discover how to invade the house
2. Find the safe box
3. Break unicode gear safe technology before the intelligent system protects itself
4. Break the safe and get the money!
5. Run away before the police arrive.

Let's analyse this

##Discover how to invade the house

Accessing the challenge with HTTP doesn't work, I used curl to get more informations
```bash
[ghozt@vps355171 ~]$ curl -v -I http://192.241.176.246:8888
* Rebuilt URL to: http://192.241.176.246:8888/
*   Trying 192.241.176.246...
* TCP_NODELAY set
* Connected to 192.241.176.246 (192.241.176.246) port 8888 (#0)
> HEAD / HTTP/1.1
> Host: 192.241.176.246:8888
> User-Agent: curl/7.51.0
> Accept: */*
>
< HTTP/1.1 400 Bad Request
HTTP/1.1 400 Bad Request
< Sec-WebSocket-Version: 13, 6, 0
Sec-WebSocket-Version: 13, 6, 0
< X-Powered-By: Ratchet/0.3.5
X-Powered-By: Ratchet/0.3.5
```

After some searchi found a snippet :

```python
import asyncio
import websockets

async def hello():
        async with websockets.connect('ws://192.241.176.246:8888/') as websocket:
                while(1):
                        name = input("INPUT: ")
                        await websocket.send(name)
                        print("> {}".format(name))
                        greeting = await websocket.recv()
                        print("< {}".format(greeting))
asyncio.get_event_loop().run_until_complete(hello())
```

Works fine, we're in da house !

## Find the safe box

Playing with input

```bash
[ghozt@vps355171 tmp]$ python test.py
INPUT : a
> a
< 128585|untouched|untouched|untouched|untouched|untouched|untouched|untouched|
INPUT : aa
> aa
< 128585|9652|untouched|untouched|untouched|untouched|untouched|untouched|
INPUT : aaaaaa
> aaaaaa
< 128585|9652|9843|127981|127749|9874|untouched|untouched|
INPUT : aaaaaaaa
> aaaaaaaa
< 128585|9652|9843|127981|127749|9874|127286|128188|
INPUT : aaaaaaaa
> aaaaaaaa
< You see him protecting himself.
```

We need to send 8 chars, and the programm protect itself after a few of attempts.


## Break unicode gear safe technology before the intelligent system protects itself

Well, we are in front of a safe, and we have to get the combination, after many tries, it seems that the combination is reset after 
the safe protects.

Tries lead me to deduce the returned values are calculated this way: 

constant+chr(input[i])

proof : 

```
INPUT :
>
< 9940|untouched|untouched|untouched|untouched|untouched|untouched|untouched|
INPUT : a
> a
< 9843|untouched|untouched|untouched|untouched|untouched|untouched|untouched|
```

I let first input empty, then an "a", 9940-9843 = 97 = ord(a)

Okay we have to line up values to open the safe, lets try to set the first value to 0 : 

But how to do such a thing whith ord(char) value ? ===> UNICODE FTW

```
INPUT : a
> a
< 9652|untouched|untouched|untouched|untouched|untouched|untouched|untouched|

I calculate : chr(9652+ord(a))

>>> chr(9652+97)
'☕'


INPUT : ☕
> ☕
< click|untouched|untouched|untouched|untouched|untouched|untouched|untouched|
```


Well, lets "clik" all values ! 

See breakThatSafe.py

```bash
[ghozt@vps355171 tmp]$ python breakThatSafe.py
⛔🔝🆗☕🚪🍦👎⛳
< 3DS{M4st3R_0f_w3BS()c|<3t}
```

\o/


ghozt
