#!/usr/bin/python
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print("> starting server at %s : %d ..." % (UDP_IP, UDP_PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("> started server!")

while True:
        data, addr = sock.recvfrom(1024)
        print("Client %s sent: %s" % (str(addr), data))
        response = ""
        data = data.split()
        if len(data) != 3:
                response = "Please send one string and 2 numbers, in this order!"
        else:
                string = data[0]
                start = int(data[1])
                length = int(data[2])
                for i in range(start, min(start + length, len(string))):
                        response += str(string[i])
        sock.sendto("The resulted substring is %s" % response, addr)


