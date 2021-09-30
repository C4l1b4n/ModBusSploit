#!/usr/bin/python3

from core import interpreter
import sys
sys.dont_write_bytecode = True


if __name__ == "__main__":
	try:
		interpreter.start()
		interpreter.console()
	except (KeyboardInterrupt, SystemExit):
		pass
