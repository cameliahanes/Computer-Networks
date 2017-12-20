#!/usr/bin/env python
import socket
import struct

def read_string(source):
	c = ''
	s = ""
	while c != '\n':
		c = source.recv(1)
		s += c
	return s[:-1]


if __name__ == '__main__':
	try:
		server = socket.create_connection(('localhost', 6666))
	except socket.error as se:
		print("Error: " + se.strerror)
		exit(-1)
	print(server)
	s = str(raw_input("Give the string: ") + '\n')
	c = str(raw_input("Give character to search for: ") + '\n')
	server.sendall(bytes(s))
	server.sendall(bytes(c))
	answer = read_string(server)
	print(answer)
