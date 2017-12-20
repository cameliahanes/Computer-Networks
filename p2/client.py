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
		server = socket.create_connection(('localhost', 9234))
	except socket.error as se:
		print("error: " + se.strerror)
		exit(-1)
	print(server)

	message = str(raw_input("Enter the array of elements: ") + '\n')
	server.sendall(bytes(message))
	answer = read_string(server)
	print(answer)

