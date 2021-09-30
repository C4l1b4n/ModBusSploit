# ModBusSploit
Framework for ModBus TCP Industrial Protocol Exploitation.

## Description
ModBusSploit is a complete framework, written in python3, that can be used to perform both Enumeration and Exploitation phases during a Penetration Test against Modbus TCP's protocol.


## Modules
ModBusSploit is released with 11 modules that are ready-to-go!
Inside "modules" tree directory, they are located in separated folders, each one for a specific scan and/or attack type.

EXPLOIT - INJECTION
* readCoil.py : reads values from a target coil register.
* readDiscreteInput.py : reads values from a target discrete register.
* readHoldingRegister.py : reads values from a target holding register.  
* readInputRegister.py : reads values from a target input register.
* writeSingleCoil.py : writes values into a target coil register.
* writeSingleRegister.py : writes values into a target register.

EXPLOIT - DOS
* dosWriteCoils.py : performs DOS attacks through write coil's function.
* dosWriteRegisters.py : performs DOS attacks through write register's function.

AUXILIARY - SCANNER
* scanner.py : performs a threefold test to check if Modbus is running on target.
* id_fuzzer.py : performs a fuzzing attack to discover Slave's ID.

AUXILIARY - SNIFF
* arp_poisoning.py : set up a Man-In-The-Middle attack between Slave and Master. Wireshark is needed to actually sniff packets.

## Installation
You don't need installation! I hate having to install something written in python3.
You can directly download ModBusSploit and run it by using:
```
./start.py
```
### Requirments
You have to install a few libraries:
```
termcolor
importlib
secrets
ipaddress
scapy
```
You can easily speed up the process using:
```
pip3 install -r requirements.txt
```

## Usage
You can run it using:
```
./start.py
```
You can print the "helper" typing "help" inside ModBusSploit's console:
```
console()> help
====COMMANDS=====================================

help	Help menu
clear	Clear screen
exit	Exit the console
show	Displays all modules or options of a selected module
use	Load a specified module
back	Unload the current module
info	Displays information about a specified module or the loaded one
set	Sets a context-specific variable to a value
exploit	Run the loaded module
```

## Examples
For a usage example check the screenshots' folder!

## Notes
I developed this framework as thesis for my Bachelor degree in Computer Engineering at Alma Mater Studiorum, Bologna, Italy.

## License
This project is licensed under MIT License - see the LICENSE.md file for details.

