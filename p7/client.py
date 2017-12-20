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
		server = socket.create_connection(('localhost', 7777))
	except socket.error as se:	
		print("Error: " + se.strerror)
		exit(-1)
	print(server)	
	s = str(raw_input("Enter the string: ") + '\n')
	a = str(raw_input("Enter the starting index: ") + '\n')
	b = str(raw_input("Enter the length of the substring: ") + '\n')
	server.sendall(bytes(s))		
	server.sendall(bytes(a))
	server.sendall(bytes(b))
	answer = read_string(server)
	print(answer)
