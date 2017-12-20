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
	a = read_string(client)
	b = read_string(client)

	try:
		a = int(a)
	except Exception as e:
		client.sendall("Index must be an integer! \n Aborting ...\n")
		return
	try:
		b = int(b)
	except Exception as e:
		client.sendall("Length must be an integer! \n Aborting ... \n")
		return
	if a < 0 or a > len(s):
		client.sendall("Index exceeds string dimensions, aborting ... \n")
		return
	if a + b > len(s):
		client.sendall("Substring is not inside the dimensions of the main string \n Aborting ... \n")
		return
	res = s[a:a + b]
	client.sendall(str(res) + '\n')

if __name__ == '__main__':
	try:
		rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		rs.bind(('0.0.0.0', 7777))
		rs.listen(5)
	except socket.error as se:
		print("Error: " + se.strerror)
		exit(-1)
	while True:
		client, addr = rs.accept()
		print("Client " + str(addr) + " has connected to server ... \n" )
		#s = read_string(client)
		#a = read_string(client)
		#b = read_string(client)
		solve_client(client)
