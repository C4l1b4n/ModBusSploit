#!/usr/bin/python3

from termcolor import colored
import sys

sys.dont_write_bytecode = True

banner="""
	    __  ___          ______             _____       __      _ __ 
	   /  |/  /___  ____/ / __ )__  _______/ ___/____  / /___  (_) /_
	  / /|_/ / __ \/ __  / __  / / / / ___/\__ \/ __ \/ / __ \/ / __/
	 / /  / / /_/ / /_/ / /_/ / /_/ (__  )___/ / /_/ / / /_/ / / /_  
	/_/  /_/\____/\__,_/_____/\__,_/____//____/ .___/_/\____/_/\__/  
	                                         /_/                     
"""

def print_banner() :
	print(colored(banner,'green'))
	
if __name__ == "__main__" :
	print_banner() 
