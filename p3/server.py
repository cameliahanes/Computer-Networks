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

def solve_client(clientsocket):
	string = read_string(clientsocket)
	clientsocket.sendall(str(string[::-1]) + '\n')

if __name__ == '__main__':
	try:
		rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		rs.bind(('0.0.0.0', 1111))
		rs.listen(5)
	except socket.error as se:
		print(se.strerror)
		exit(-1)
	while True:
		clientsocket, addr = rs.accept()
		print("Client " + str(addr) + " has connected to server ... \n")
		solve_client(clientsocket)
