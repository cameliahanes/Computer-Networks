#!/usr/bin/env python
import socket
import struct

if __name__ == '__main__':
	server_ip = 'localhost'
	server_port = 5555
	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except socket.error as se:
		print(se.strerror)
		exit(-1)
	number = str(raw_input("Enter the number: ") + '\n')
	server.sendto(bytes(number), (server_ip, server_port))
	res = server.recvfrom(100)
	print(res)

