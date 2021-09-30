#!/usr/bin/python3

import sys
import os
import importlib

sys.dont_write_bytecode = True


class Command:
	commands = ['exit','help','show','use','set','exploit','info','back','clear']
	commands_helper = [
				['help','Help menu'],
				['clear','Clear screen'],
				['exit','Exit the console'],
				['show','Display all modules or options of a selected module'],
				['use','Load a specified module'],
				['back','Unload the curret module'],
				['info','Display information about a specified module or the loaded one'],
				['set','Set a context-specific variable to a value'],
				['exploit','Run the loaded module']
			]
	loaded_module=''
	name_loaded_module=''
			
	def exit(user_input):
		if len(user_input)!=1:
			print("[-] Did you mean 'exit' ?")
		else:
			print("\n[!] Thanks for using ModBusSploit! [!]\n")
			sys.exit(0)
	
	def help(user_input):
		if len(user_input)!=1:
			print("[-] Did you mean 'help' ?")
		else:
			print("====COMMANDS=====================================\n")
			for command in Command.commands_helper:
				print(command[0]+"	"+command[1]+"")
			print("\n")

	def show(user_input):
		if len(user_input) > 2 or len(user_input)==1:
			print("[-] You should specify 'show modules' or 'show options'")
		else:
			if user_input[1] == 'modules':
				location = 'modules'
				for path, nothing, files in os.walk(location):
					for name in files:
						print(os.path.join(path, name.split('.')[0]))
			elif user_input[1] == 'options':
				if Command.loaded_module == "" :
					print("[-] You should use a module first...")
				else:
					options = Command.loaded_module.options
					dash = '-' * 60
					info_list=['Name','Value','Info']
					print(dash)
					print('{:<20s}{:<20s}{:<20s}'.format(info_list[0],info_list[1],info_list[2]))
					print(dash)
					for i in range(len(options)):
					      print('{:<20s}{:<20s}{:<20s}'.format(options[i][0],options[i][1],options[i][2]))
					print("\n")
			else:
				print("[-] You should specify 'show modules' or 'show options'")
	def use(user_input):
		if len(user_input) > 2 or len(user_input)==1:
			print("[-] You should specify one module")
		else:
			try:
				module = user_input[1].replace('/','.')
				Command.loaded_module = importlib.import_module(module)
				Command.name_loaded_module = module.split('.')[-1]
			except:
				print('[-] Module not found...')
	def set(user_input):
		if Command.loaded_module == '':
			print("[-] You should specify one module")
		elif len(user_input) != 3:
			print("[-] You should use 'set <parameter> <value>' ")
		else:
			options = Command.loaded_module.options
			parameter = user_input[1]
			for i in range (0,len(options)):
				if options[i][0] == parameter :
					parameter = i
					break
			if  parameter == user_input[1] :
				print("[-] You should specify a valid parameter")
			else:
				Command.loaded_module.options[i][1] = user_input[2]
				print("[+] "+str(user_input[1])+" set to "+str(user_input[2]))


	def exploit(user_input):
		if len(user_input)!=1:
			print("[-] Did you mean 'exploit' ?")
		elif Command.loaded_module == '':
			print("[-] You should specify one module")
		else:
			Command.loaded_module.main()
	
	def info(user_input):
		if len(user_input) > 2 :
			print("[-]Did you mean 'info' or 'info <module>' ?")
		elif len(user_input)==1 and Command.loaded_module=='' :
			print("[-] You should use one module or use 'info <module>'")
		elif len(user_input)==1 and Command.loaded_module!='' :
			Command.loaded_module.show_info()
		else:
			try:
				module = user_input[1].replace('/','.')
				Command.loaded_module = importlib.import_module(module)
				Command.loaded_module.show_info()
				Command.loaded_module = ''
			except:
				print('[-] Module not found...')
			

	def back(user_input):
		if len(user_input)!=1:
			print("[-] Did you mean 'back' ?")
		else:
			Command.name_loaded_module=''
			Command.loaded_module=''
			
	def clear(user_input):
		if len(user_input)!=1:
			print("[-] Did you mean 'clear' ?")
		else:
			try:
				os.system('clear')
			except:
				try:
					os.system('cls')
				except:
					print("[!] Command unsupported ... ")
