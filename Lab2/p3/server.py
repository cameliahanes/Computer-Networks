#!/usr/bin/env python
import socket
import struct
import sys
import time
import random
import threading

INT = 4
INF = 2 ** 30
random.seed()
refnr = random.randint(0, 1001)
lock = threading.Lock()
winner_player = None
timeout = threading.Event()
winner_elected = threading.Event()
winner_elected.clear()
players = []
player_count = 0
mindif = INF
rs = None

def set_timeout():
	global timeout
	timeout.set()

timer = threading.Timer(5, set_timeout)

def player_behaviour(playernr, playeraddr):
	global lock, player_count, winner_player, timeout, mindif, winner_elected, rs
	myself = player_count
	print("Player #{} from {}".format(myself, playeraddr))
	greeting = "Player #{}\n".format(myself)
	rs.sendto(bytes(greeting), playeraddr)
	playernr = struct.unpack('!I', playernr)[0]
	timeout.wait()
	lock.acquire()
	if abs(playernr -refnr) < mindif:
		mindif = abs(playernr - refnr)
		winner_player = myself
	player_count -= 1
	if player_count == 0:
		winner_elected.set()
	lock.release()
	
	winner_elected.wait()
	if myself == winner_player:
		print("Winner player #{}:\n".format(winner_player))
		rs.sendto(bytes('You won with a difference of: {}\n'.format(mindif)), playeraddr)
	else:
		rs.sendto(bytes('You lost with a difference of: {}\n'.format(abs(playernr - refnr))), playeraddr)



def reset_game():
	global lock, players, winner_player, player_count, refnr, timeour, mindif, winner_elected
	while True:
		print('-'*40)
		timeout.wait()
		for player in players:
			player.join()
		timeout.clear()
		lock.acquire()
		players = []
		player_count = 0
		winner_elected.clear()
		winner_player = None
		refnr = random.randint(0, 1001)
		mindif = INF
		print('They have to guess this: ', refnr)
		lock.release()

if __name__ == '__main__':
	try:
		rs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		rs.bind(('0.0.0.0', 3333))
	except socket.error as se:
		print("Error :" + se.strerror)
		exit(-1)
	print(socket.gethostname())
	print("They have to guess this: " + str(refnr))
	referee = threading.Thread(target = reset_game)
	referee.start()
	
	while True:
		data, addr = rs.recvfrom(INT)
		player = threading.Thread(target = player_behaviour, args = (data,  addr))
		players.append(player)
		player_count += 1
		player.start()
		timer.cancel()
		timer = threading.Timer(5, set_timeout)
		timer.start()
	

