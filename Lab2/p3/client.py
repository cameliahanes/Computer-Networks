#!/usr/bin/env python
import socket
import sys
import time
import struct
import random

INT = 4

if __name__ == '__main__':
	ip = 'localhost'
	port = 3333
	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except socket.error as se:
		print("Error: " + se.strerror)
		exit(-1)
	
	random.seed()
	myguess = random.randint(0, 1001)
	print('My guess: {}.'.format(myguess))
	try:
		server.sendto(struct.pack('!I', myguess), (ip, port))
	except socket.error as se:
		print("Error: " + se.strerror)
		exit(-2)
	greeting, addr = server.recvfrom(100)
	print(greeting + "\n")
	
	print("Waiting for answer ... \n")
	answer, addr = server.recvfrom(100)
	print(answer)
	server.close()
