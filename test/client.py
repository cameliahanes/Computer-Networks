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
	
	host = '127.0.0.1'
	port = 1234
	buffsize = 100
	
	message = str(raw_input("Enter the computer name / exit to exit: ") + '\n')
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((host, port))
	
	while message != "exit":
		client.send(message)
		data = client.recv(buffsize)
		print("Received answer: " + str(data) + '\n')
		message = str(raw_input("Enter exit to exit / message - comp name - to continue: "))
	
	client.close()


