from math import sqrt
from random import randint, choice, shuffle
import hashlib
import sys
import json
from collections import OrderedDict
import socket
from Crypto import Random
from Crypto.Cipher import AES

pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
unpad = lambda s : s[0:-ord(s[-1])]

def encrypt(message, key):
    message = pad(message)
    print message
    IV = Random.new().read(AES.block_size)
    aes= AES.new(key, AES.MODE_CBC, IV)
    return "%s%s" % (IV, aes.encrypt(message))

def decrypt(message, key):
    IV = message[:AES.block_size]
    aes = AES.new(key, AES.MODE_CBC, IV)
    return unpad(aes.decrypt(message[AES.block_size:]))

server = "0.0.0.0"
is_server = True
selectected_key = 0
shared_secret = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def generate_challenges():
    challenges = {}
    for i in xrange(512):
        challenges[i] = ''.join(choice(''.join([chr(_) for _ in xrange(0, 255)])) for x in range(AES.block_size))
    items = challenges.items()
    shuffle(items)
    challenges = OrderedDict(items)
    return challenges

def cipher(challenge):
    key = choice(''.join([chr(_) for _ in xrange(0, 255)])) * 16
    return encrypt(challenge, key)

def serialize_challenge(challenges):
    message = []
    for k, v in challenges.items():
        data = cipher('OK%s%s' % (k,v)).encode("hex")
        message.append(data)
    return json.dumps(message)

if __name__ == "__main__":

    if len(sys.argv) > 1:
        server = sys.argv[1]
        is_server = False

    # Prepare exchange    
    try:
        if is_server:
            challenges = generate_challenges()
            serialized_challenges = serialize_challenge(challenges)
            print("Start server")
            
            s.bind((server, 31337))
            while True:
                s.listen(5)
                client, accept = s.accept()

                # set exchange
                client.send(serialized_challenges)
                shared_secret = challenges[int(client.recv(32))]
                print("Key exchange completed")

                while True:
                    secret_message = client.recv(1024)
                    message = decrypt(secret_message, shared_secret)
                    print("<<< %s" % message)
                    message = raw_input(">>> ")
                    secret_message = encrypt(message, shared_secret)
                    client.send(secret_message)
        else:
            print("Connect to %s" % server)
            s.connect((server, 31337))
            while True:
                challenges = s.recv(51200)
                # set exchange
                challenges = json.loads(challenges)
                selected_challenge = choice(challenges)

                #BF challenge and send id
                for k in xrange(0, 255):
                    key = chr(k) * 16
                    try:
                        unciphered = decrypt(selected_challenge.decode("hex"), key)
                        if unciphered.startswith("OK"):
                            selected_challenge = unciphered
                            break
                    except TypeError:
                        pass
                key_index = selected_challenge[2:-16]
                shared_secret = selected_challenge[-16:]
                s.send(key_index)

                print("Key exchange completed")

                while True:
                    message = raw_input(">>> ")
                    secret_message = encrypt(message, shared_secret)
                    s.send(secret_message)
                    secret_message = s.recv(1024)
                    message = decrypt(secret_message, shared_secret)
                    print("<<< %s" % message)

    except:
        s.close()