#!/usr/bin/env python
import struct
import socket

def read_string(source):
	c = ''
	s = ""
	while c != '\n':
		c = source.recv(1)		
		s += c
	return s[:-1]

def solve_client(client):
	number = int(read_string(client))
	div = 2
	res = ""
	while div <= number/2:
		if number % div == 0 :
			res += str(div)
			res += " "
		div += 1
	client.sendall(str(res) + '\n')

if __name__ == '__main__':
	try:
		rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		rs.bind(('0.0.0.0', 5555))
		rs.listen(5)
	except socket.error as se:
		print("Error: " + se.strerror)
		exit(-1)
	while True:
		client, addr = rs.accept()
		print("Client: " + str(addr) + " has connected to server ... \n")
		solve_client(client)

