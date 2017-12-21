#!/usr/bin/env python
import socket
import struct

def solve_client(client, number):
	div = 2
	ans = ""
	#print(number)
	number = int(number)
	while div <= number / 2:
		if number % div == 0:
			ans += str(div);
			ans += " "
			div = int(div)
		div += 1
	ans += '\n'
	rs.sendto(bytes(str(ans)), client)

if __name__ == '__main__':
	try:
		rs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		rs.bind(('0.0.0.0', 5555))
	except socket.error as se:
		print(se.strerror)
		exit(-1)
	while True:
		number, addr = rs.recvfrom(100)
		print(addr, number)
		solve_client(addr, number)	

