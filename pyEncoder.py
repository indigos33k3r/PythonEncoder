#!/usr/bin/python
import os
import sys

def cleanterminal():
	'''
	Makes our terminal clean and nice
	'''
	os.system("cls" if os.name == "nt" else "clear")

def encoder():
	'''
	Get user input and format it like shellcode \x70\x72\x69\x6e\x74\
	'''
	userinput = raw_input("[+] Enter python code: ")
	formated = "\\x" + "\\x".join("{0:x}".format(ord(userinput)) for userinput in userinput)

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
		print "[+] Crafting encoded python script"
		file=open("code.py","w")
		file.write("\ncode =('{0}'); exec(code)".format(formated))
		file.close()
		print "[+] Successfully crafted encoded python script"
	except:
		print "[-] Error creating crafted python script"	

if __name__ == '__main__':
	'''
	Run our functions
	'''
	cleanterminal()
	encoder()