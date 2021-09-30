#!/usr/bin/python3
import socket
import sys
import secrets
import ipaddress
from time import sleep

transaction_identifier = b""
protocol_identifier = b"\x00\x00"
lenght_field = b"\x00\x00"
slave_address = b"\x01"		
mod_function = b"\x43"			
data = b""


options = [
		['address','','Target address or addresses in CIDR notation to be scanned.'],
		['port','502','Target port to be scanned. Default: 502']	
	]

def show_info():
	print("This module can discover hosts that are running ModBus.")

def main():
	ip_range = options[0][1]
	port = options[1][1]
	
	if port == '' or ip_range == '':
		print("[!] You should specify all parameters...")
		return None
	elif int(port) < 1 or int(port) > 65535 or not port.isnumeric():
		print("[!] You specified a wrong port...")
		return None
		
	try:
		targets = ipaddress.IPv4Network(ip_range)

	except:
		print("[!]Wrong ip or ip range provided")
		return None

	print("[*] Scan started...\n")
	for address in targets:
		
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
			s.settimeout(1)
			transaction_identifier = secrets.token_bytes(2)
			payload = transaction_identifier + protocol_identifier +lenght_field + slave_address + mod_function + data
			s.connect((str(address),int(port)))
			s.send(payload)
			response = s.recv(256)
			s.close()

			if (response[0:2] == transaction_identifier) :
				tested = 1
				
				while(tested<3):
					sleep(1)

					try:
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
						s.settimeout(1)
						transaction_identifier = secrets.token_bytes(2)
						payload = transaction_identifier + protocol_identifier +lenght_field + slave_address + mod_function + data
						s.connect((str(address),int(port)))
						s.send(payload)
						response = s.recv(256)
						s.close()
					
						if (response[0:2] == transaction_identifier) :
							tested = tested + 1
						else :
							break
					except:
						break

				print("[+] "+str(address)+" is probably running ModBus. Successful tests: ["+str(tested)+"/3]")
		except KeyboardInterrupt :
			print("\n")
			return None
		except:
			pass
	print("\n[*] Scan completed!")

if __name__ == "__main__":
	main()
