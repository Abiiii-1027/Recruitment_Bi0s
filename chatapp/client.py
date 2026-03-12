import socket

CAESAR_KEY = 7
XOR_KEY = b"secretkey"

def caesar_encrypt(data):
    return bytes((b + CAESAR_KEY) % 256 for b in data)

def caesar_decrypt(data):
    return bytes((b - CAESAR_KEY) % 256 for b in data)

def xor_encrypt(data):
    return bytes(data[i] ^ XOR_KEY[i % len(XOR_KEY)] for i in range(len(data)))

xor_decrypt = xor_encrypt

def encrypt(data):
    return xor_encrypt(caesar_encrypt(data))

def decrypt(data):
    return caesar_decrypt(xor_decrypt(data))

client = socket.socket()
client.connect(("localhost", 900))

while True:
    message = input("You:")
    client.send(encrypt(message.encode()))
    if message.lower() == "exit":
        print("exitting the chat")
        break
    response = decrypt(client.recv(1024)).decode()
    if response.lower() == "exit":
        print("server exited the chat")
        break

client.close()