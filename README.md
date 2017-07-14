# PythonEncoder

#### Example
```
C:\>pyEncoder.py

[+] Enter python code: print ("hello world")
[+] Cleaning first
[+] Cleaning done
[+] Crafting encoded python script
[+] Successfully crafted encoded python script

C:\>type code.py

code =('\x70\x72\x69\x6e\x74\x28\x22\x68\x65\x6c\x6c\x6f\x77\x6f\x72\x6c\x64\x22\x29'); exec(code)

C:\>python code.py
hello world
```
