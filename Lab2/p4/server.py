#!/usr/bin/env python
import socket
import struct

def solve_client(client, s1, s2):
	i = 0
	j = 0
	s3 = ""
	while i < len(s1) and j < len(s2):
		if s1[i] < s2[j]:
			s3 += str(s1[i])
			i += 1
		elif s1[i] > s2[j]:
			s3 += str(s2[j])	
			j += 1
		else:
			s3 += str(s1[i])
			i += 1
			j += 1
	while i < len(s1):
		s3 += str(s1[i])
		i += 1
	while j < len(s2):
		s3 += str(s2[j])
		j += 1
	rs.sendto(bytes(str(s3)), client)
	
if __name__ == '__main__':
	try:
		rs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		rs.bind(('0.0.0.0', 4444))
	except socket.error as se:
		print(se.strerror)
		exit(-1)
	while True:
		s1, addr = rs.recvfrom(100)
		s2, addr = rs.recvfrom(100)
		print(addr, s1, s2)
		solve_client(addr, s1, s2)


