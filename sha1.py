#_*_coding=UTF-8_*_
# copyright 2019 BILLAL FAUZAN
# Karya Anak Bangsa
# MD5 DENCRYPT Offline 90%

"""
NOTE:
	Please Abang Eneng Jangan Ubah Source Code Ny
	Saya Susah Payah Membuat Program Ini
	Saya Sengaja Open Source Supaya Anak Indonesia Bisa Membuat Program Sendiri

	Jadi
	Jangan Di Recode Bangsat!!
"""
__banner__ = """\033[31;1m
    __  __           __    ____
   / / / /___ ______/ /_  / __ \___  _____
  / /_/ / __ `/ ___/ __ \/ / / / _ \/ ___/\033[37;1m
 / __  / /_/ (__  ) / / / /_/ /  __/ /__
/_/ /_/\__,_/____/_/ /_/_____/\___/\___/\033[33;1m
     copyright 2019 Billal Fauzan
\033[32;1m
INFO:\033[34;1m
    Author \033[31;1m:\033[32;1m Billal Fauzan\033[34;1m
    Version\033[31;1m:\033[32;1m 1.0\033[34;1m
    Name  \033[31;1m :\033[32;1m Hash Dencrypter Offline 50%\033[34;1m
    Team  \033[31;1m :\033[32;1m Woll Cyber Team, Black Coder Crush\033[34;1m
    Link To Download \033[31;1m:\033[32;1m bit.ly/passwordhashdec\033[0m

"""
try:
	import os,sys,time,hashlib
	from prompt_toolkit import prompt
except Exception as E:
	print ("[Err]: "+str(E))
	sys.exit()

def dencrypt(hash,password):
	try:
		sys.stdout.write("\n\033[34;1m[\033[33;1m!\033[34;1m] \033[33;1mTrying: \033[31;1m"+str(password))
		sys.stdout.flush()
#		time.sleep(0.1)
		sha1 = hashlib.sha1()
		sha1.update(bytes(str(password),"utf-8"))
		md = sha1.hexdigest()
		if hash == md:
			print ("\033[34;1m\n[\033[32;1m+\033[34;1m] \033[37;1mFound: \033[32;1m"+str(password))
			print ("\033[0m")
			sys.exit()
	except Exception as E:
		print ("[Err]: "+str(E))
#		print ("\033[31;1m[-] unknown error\033[0m")
		sys.exit()

def main():
	os.system("clear")
	print (__banner__)
	hash = input("[?] Hash: ")
	wordlist =""
	while True:
		p = input("[?] Wordlist Default? (Y/n): ")
		if p in ["Y","y"]:
			wordlist = "password.txt"
			break
		elif p in ["N","n"]:
			wordlist = input("[?] Wordlist: ")
			break
	try:
		pw = open(wordlist,"r").read()
		for password in pw.splitlines():
			dencrypt(hash,password)
	except IOError:
		print ("[Err]: File %s not found"%(wordlist))
		sys.exit()

def login():
	os.system("clear")
	print (__banner__)
	pwd = "6d845a610cf2ff6872a04239349251e4"
	print ("[*] Please contact author to find out the password")
	pw = prompt("[?] Password to unlock: ",is_password=True)
	m = hashlib.md5()
	m.update(bytes(pw,"utf-8"))
	md = m.hexdigest()
	if pwd == md:
		main()
	else:
		print ("[*] Please contact author to find out the password")
login()
