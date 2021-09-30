#!/usr/bin/python3

from core.banner import *
from core.info import *
from core.commands import Command
from termcolor import colored
import sys

sys.dont_write_bytecode = True

def start():
	print("")
	print_banner()
	print("")
	print_info()
	print("")

def console():
	while True:
		user_input = input("console("+colored(Command.name_loaded_module,'red')+")> ").strip().split()
		if len(user_input) == 0:
			pass
		else:
			if user_input[0] in Command.commands :
				result = getattr(Command, user_input[0])(user_input)
			else:
				print("[!] Command not supported... try 'help'")
