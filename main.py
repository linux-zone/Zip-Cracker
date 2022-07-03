#!/usr/bin/python3
# <-- Mr Shell -->
from zipfile import ZipFile
from tempfile import mkdtemp
import time, os

os.system('clear' if os.name == 'posix' else 'cls')
print('''\x1b[1;35m
 ______        ____                _
|__  (_)_ __  / ___|_ __ __ _  ___| | _____ _ __
  / /| | '_ \| |   | '__/ _` |/ __| |/ / _ \ '__|
 / /_| | |_) | |___| | | (_| | (__|   <  __/ |
/____|_| .__/ \____|_|  \__,_|\___|_|\_\___|_|
       |_|\x1b[00m

     \x1b[33m[+] Creator:  \x1b[36m [ Mr-shell              ]
     \x1b[33m[+] Github:   \x1b[36m [ Github.com/Linux-Zone ]
     \x1b[33m[+] Telegram: \x1b[36m [ T.me/Linux_Zone_Org   ]
''')


zip_file = input('\x1b[91m>> \x1b[94mEnter zip file path: \x1b[00m')
password_list = open(input('\x1b[91m>> \x1b[94mEnter password list file path: \x1b[00m'), "r").read().splitlines()
temp_directory = mkdtemp()
start = time.time()
found = False

for password in password_list:
	try:
		zipfile = ZipFile(zip_file)
		zipfile.extractall(temp_directory, pwd=password.encode('utf-8'))
		found = True
		print("\n\x1b[92mPassword Found: \x1b[00m{}".format(password))
		end = time.time()
		print("\x1b[92mSpeed: \x1b[00m{}ms\n".format(str(end - start)[:4]))
		time.sleep(1)
		break
	except:
		pass

if not found:
	print("\n\x1b[91mPassword not found ;)\x1b[00m\n")
	time.sleep(1)

exit()
