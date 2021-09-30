#!/usr/bin/python3

import socket
from time import sleep
import sys


options = [
		['address','','Target address to be fuzzed.'],
		['port','502','Target port to be scanned. Default: 502']	
	]

def show_info():
	print("This module can fuzz slave's id. Default one is 1 but it can be changed for many purposes.")

def main():
	address = options[0][1]
	port = options[1][1]
	
	if port == '' or address == '':
		print("[!] You should specify all parameters...")
		return None
	elif int(port) < 1 or int(port) > 65535 or not port.isnumeric():
		print("[!] You specified a wrong port...")
		return None
		

	print("[*] Bruteforcing slave's ID...\n")
	try:
		for i in range (0,256):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
			s.settimeout(1)
			s.connect((address,int(port)))

			payload=b"\x18\x21\x00\x00\x00\x02"+bytes([i])+b"\x01"
			s.send(payload)
			a = s.recv(256)
			print("\r[*]Testing ID: "+str(i), end='')
			sleep(0.4)

			if (len(a) > 0 and (a[0:4] == b"\x18\x21\x00\x00")):
				print("\r                         ", flush=True, end='')
				print("\r[+]ID FOUND: " +str(i), end='\n')
				break
			
			s.close()
	except KeyboardInterrupt :
		print("\n")
		return None
	except:
		print("[-] Host is offline or you specified a wrong port...")
		
if __name__ == "__main__" :
	main()
