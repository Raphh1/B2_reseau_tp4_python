import socket
import re


def evaluer_operation(operation):
    try:
        
        resultat = eval(operation)
        return str(resultat)
    except:
        return "Erreur dans l'opération"


def serveur():
   
    serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur_socket.bind(('192.168.185.4', 13337))
    serveur_socket.listen(5)

    print("Le serveur écoute sur le port 12345...")

    while True:
        client_socket, _ = serveur_socket.accept()
        print("Nouvelle connexion reçue.")

       
        operation = client_socket.recv(1024).decode('utf-8')

        
        pattern = re.compile(r'^[+-]?\d+\s*[\+\-\*]\s*[+-]?\d+$')
        if not re.match(pattern, operation):
            client_socket.send("Opération non valide.".encode('utf-8'))
            client_socket.close()
            continue

        
        resultat = evaluer_operation(operation)
        client_socket.send(resultat.encode('utf-8'))

        
        client_socket.close()

if __name__ == "__main__":
    serveur()
