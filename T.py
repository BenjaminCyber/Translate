from termcolor import colored
from googletrans import Translator
import os
from time import sleep
import var_animate

banner = var_animate.banner('TRANSLATOR','By BENJAMIN','0.1')
def bahan():
	os.system('pip install termcolor')
	os.system('pip install googletrans')
	print(colored("INSTALLED",'red'))
	os.system('pip install VarAnimate')
	ok()
def eng():
	c =input(colored("MASUKAN KALIAMAT:",'blue'))
	i = Translator()
	hasil = i.translate(c, src= 'id', dest= 'en')
	print(colored(f"{hasil.src}",'red'))
	print(colored(f"{hasil.dest}",'blue'))
	print(colored(f"{hasil.origin} >> {hasil.text}",'green'))
def males():
	y =input(colored("MASUKAN KALIMAT:",'blue'))
	s = Translator()
	data = s.translate(y, src= 'en', dest= 'id')
	print(colored(f"{data.src}",'red'))
	print(colored(f"{data.dest}",'blue'))
	print(colored(f"{data.origin} >> {data.text}",'green'))
def ok():
	print(colored("JANGAN LUPA SUBSCRIBE",'red'))
	print(colored("[1]. INDONESIA > ENGLISH",'blue'))
	print(colored("[2].  ENGLISH > INDONESIA",'red'))
	print(colored("[3].  INSTALL BAHAN",'green'))
	pil = input(colored("MASUKAN PILIHAN:",'green'))
	if (pil == '1'):
		eng()
	elif (pil == '2'):
		males()
	elif (pil == '3'):
		bahan()
	else:
		print("INPUT SALAH")
		sleep(2)
		ok()
os.system('clear')
print(colored("SUBSCRIBE BRO PLISSSSS",'blue'))
os.system('xdg-open https://youtu.be/TfPKZTK4_Qw')
print("GA SUBSCRIBE GA JALAN")
sleep(5)
print(banner)
ok()
