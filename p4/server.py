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

def solve_client(client):
	s1 = read_string(client)
	s2 = read_string(client)
	s3 = ""
	i = 0
	j = 0
	while i < len(s1) and j < len(s2):
		if s1[i] < s2[j]:
			s3 += s1[i]
			i += 1
		else:
			if s2[j] < s1[i]:
				s3 += s2[j]
				j += 1
			else:
				s3 += s1[i]
				i += 1
				j += 1
	while i < len(s1):
		s3 += s1[i]
		i += 1
	while j < len(s2):
		s3 += s2[j]
		j += 1

	client.sendall(str(s3) + '\n')	
	

if __name__ == '__main__':
	try:
		rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		rs.bind(('0.0.0.0', 4444))
		rs.listen(5)
	except socket.error as se:
		print("Error: " + se.strerror + '\n')
		exit(-1)
	while True:
		client, addr = rs.accept()
		print("Client " + str(addr) + " has connected to server... \n")
		solve_client(client)


