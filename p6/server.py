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

def solve_client(client):
	s = read_string(client)
	c = read_string(client)
	res = ""
	for i in range (len(s)):
		if s[i] == c:
			res += str(i)
			res += " "
	client.sendall(str(res) + '\n')

if __name__ == '__main__':
	try:
		rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		rs.bind(('0.0.0.0', 6666))
		rs.listen(5)
	except socket.error as se:
		print("Error: " + se.strerror)
		exit(-1)
	while True:
		client, addr = rs.accept()
		print("Client " + str(addr) + " connected to server .. \n")
		solve_client(client)

