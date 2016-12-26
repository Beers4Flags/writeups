#!/usr/bin/env python

import asyncio
import websockets
import time

async def hello():
        async with websockets.connect('ws://192.241.176.246:8888/box') as websocket:
                name = "aaaa"
                await websocket.send(name)
                greeting = await websocket.recv()
                splitted = greeting.split("|")
                char1 = chr(int(splitted[0])+97)
                char2 = chr(int(splitted[1])+97)
                char3 = chr(int(splitted[2])+97)
                char4 = chr(int(splitted[3])+97)
                half = char1+char2+char3+char4
                await websocket.send(half+"aaaa")
                greeting = await websocket.recv()
                splitted = greeting.split("|")
                char5 = chr(int(splitted[4])+97)
                char6 = chr(int(splitted[5])+97)
                char7 = chr(int(splitted[6])+97)
                char8 = chr(int(splitted[7])+97)
                otherhalf = char5+char6+char7+char8
		print("half+otherhalf")
                await websocket.send(half+otherhalf)
                greeting = await websocket.recv()
                print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())

