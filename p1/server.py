#!/usr/bin/env python
import socket
import struct

print(socket.gethostname())

def read_string(source):	
	c = ''
	s = ""
	while c != '\n':
		c = source.recv(1)
		s += c
	return s[:-1]

def solve_client(client):
	string = read_string(client)
	arr = string.split()
	sum = 0
	for elem in arr:
		if elem == ' ':
			sum += 1
	client.sendall(str(sum) + '\n')

if __name__ == '__main__':
	try:
		rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		rs.bind(('0.0.0.0', 7777))
		rs.listen(5)
	except socket.error as se:
		print(se.strerror)
		exit(-1)
	while True:
		clientsock, addr = rs.accept()
		print("Client: " + str(addr) + " has connected \n")
		solve_client(clientsock)


