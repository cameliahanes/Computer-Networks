#!/usr/bin/env python
import socket

host = "127.0.0.1"
port = 2004
BUFFER_SIZE = 20
message = raw_input("tcpClientA: Enter message / Enter exit: ")

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

while message != 'exit':
	tcpClientA.send(message)
	data = tcpClientA.recv(BUFFER_SIZE)
	print(" Client2 received data: " +  data)
	message = raw_input("tcpClientA: Enter message to continue / Enter exit : ")

tcpClientA.close()

