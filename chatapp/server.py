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

server = socket.socket()
server.bind(("localhost", 900))
server.listen(1)

conn, addr = server.accept()
print("Connection established with", addr)

while True:
    msg = decrypt(conn.recv(1024)).decode()
    if msg.lower() == "exit":
        break
    print("client", msg)
    print("Type exit to end the chat")
    response = input("You:")
    conn.send(encrypt(response.encode()))
    if response.lower() == "exit":
        print("exited the chat")
        break

conn.close()
