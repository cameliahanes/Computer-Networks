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
		server = socket.create_connection(('localhost', 4444))
	except socket.error as se:
		print("Error: " + se.strerror)
		exit(-1)
	s1 = str(raw_input("Enter first sorted string: ") + '\n')
	s2 = str(raw_input("Enter the second sorted string: ") + '\n')
	server.sendall(bytes(s1))
	server.sendall(bytes(s2))
	answer = read_string(server)	
	print(answer)

