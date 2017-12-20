#!/usr/bin/env python
import socket
import struct

def read_string(source):
	s = ""
	c = ''
	while c != '\n':
		c = source.recv(1)
		s += c
	return s[:-1]


if __name__ == '__main__':
	try:
		server = socket.create_connection(('localhost', 5555))
	except socket.error as se:
		print("Error: " + se.strerror)
		exit(-1)
	print(server)
	number = str(raw_input("Enter the number: ") + '\n')
	server.sendall(bytes(number))
	answer = read_string(server)
	print(answer)
