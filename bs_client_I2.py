import socket
from sys import exit


host = '192.168.185.4'  
port = 13337             


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    s.connect((host, port))
    message = input("Que veux-tu envoyer au serveur : ")
except:
    print("il semble y avoir une erreur")
    exit(1)




s.sendall(message.encode("utf-8"))


data = s.recv(1024)


s.close()


print(f"Le serveur a répondu {repr(data)}")

exit(0)