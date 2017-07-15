#!/usr/bin/python
import os
import sys

def cleanterminal():
	'''
	Makes our terminal clean and nice
	'''
	os.system("cls" if os.name == "nt" else "clear")
	
def banner():
	'''
	Print banner and info how to use the script
	'''
	print "             _____                    _ "
	print "            |  ___|                  | |"         
	print " _ __  _   _| |__ _ __   ___ ___   __| | ___ _ __"
	print "| '_ \| | | |  __| '_ \ / __/ _ \ / _` |/ _ \ '__|"
	print "| |_) | |_| | |__| | | | (_| (_) | (_| |  __/ |"
	print "| .__/ \__, \____/_| |_|\___\___/ \__,_|\___|_|"  
	print "| |     __/ |"  
	print "|_|    |___/\n"                              

def encoder():
	'''
	Get user input and format it like shellcode \x70\x72\x69\x6e\x74\
	'''
	usrinput = raw_input("[+] Enter code: ")
	formated = "\\x" + "\\x".join("{0:x}"
				.format(ord(usrinput)) for usrinput in usrinput)

	'''
	Delete the file before we create a new one
	'''
	try:
		print "[+] Cleaning first"
		os.remove("code.py")
		print "[+] Cleaning done"
	except:
		pass
	
	'''
	Create a new file with the encoded content
	'''
	try:
		print "[+] Crafting python script"
		file=open("code.py","w")
		file.write("\ncode =('{0}'); exec(code)".format(formated))
		file.close()
		print "[+] Successfully crafted python script"
	except:
		print "[-] Error crafting python script"	

if __name__ == '__main__':
	'''
	Run our functions
	'''
	cleanterminal()
	banner()
	encoder()
