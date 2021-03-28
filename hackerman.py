# hackerman script by daniel
# change fakecodeAddress to text file desired (update encoding if necessary)
# press Esc key to exit.

import msvcrt as msv
import sys
import time
import os

dirAddress = os.path.dirname(__file__)
fakecodeAddress = dirAddress + "/fakecodes/fakecode_shrek.txt"
fakecodeString = open(fakecodeAddress, encoding="utf8").read()		# import fake code

speed = 6;		# chars per keypress (always multiple of keymult!!)
keymult = 2;	# chars per tick (always <= speed!!) 
n = 0;
skip_count = 0;

while True:
	if msv.kbhit():
		chr_ = msv.getch()
		if chr_ == chr(27).encode(): # Esc key pressed
			break;
			
		else:
			sp_tol = 3 # space tolerance; if this no. of spaces (or tabs) ahead then skip them.
			n_aux = n
			while fakecodeString[n_aux:n_aux+sp_tol] == "   " or fakecodeString[n_aux:n_aux+sp_tol] == "			":
				skip_count += sp_tol;
				n_aux += sp_tol;
		
			m = 0;
			while (m < speed + skip_count):
				if msv.kbhit() == False:
					print(fakecodeString[n+m:n+m+keymult], end = "")
					sys.stdout.flush()
					m += keymult;
					time.sleep(0.001)
				else:
					print(fakecodeString[n+m:n+speed+skip_count], end = "")
					sys.stdout.flush()
					break;
				
		n += speed + skip_count;
		skip_count = 0;