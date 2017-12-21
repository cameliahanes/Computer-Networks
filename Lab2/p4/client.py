#!/usr/bin/env python
import socket
import struct

if __name__ == '__main__':
	server_ip = 'localhost'
	server_port = 4444
	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except socket.error as se:
		print(se.strerror)
		exit(-1)
	s1 = str(raw_input("Enter the first sorted string: ") + '\n')
	s2 = str(raw_input("Enter the second sorted string: ") + '\n')
	server.sendto(bytes(s1), (server_ip, server_port))
	server.sendto(bytes(s2), (server_ip, server_port))
	s3, addr = server.recvfrom(100)
	print(s3)
