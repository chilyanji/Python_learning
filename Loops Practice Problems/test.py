import socket

HOST = "10.48.177.53"
PORT = 1337

s = socket.socket()
s.connect((HOST, PORT))

data = s.recv(4096).decode()
print(data)

enc_hex = data.split(": ")[1].strip()

plaintext = "THM{thisisafakeflag}"
cipher = bytes.fromhex(enc_hex)

key = "".join(chr(cipher[i] ^ ord(plaintext[i])) for i in range(len(plaintext)))[:5]

print("Key:", key)

s.send((key + "\n").encode())

print(s.recv(4096).decode())