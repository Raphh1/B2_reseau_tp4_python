import socket

# Fonction principale du client
def client():
    # Initialisation du client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.185.4', 13337))

    # Demande à l'utilisateur de saisir une opération arithmétique
    operation = input("Entrez une opération arithmétique : ")

    # Envoi de l'opération au serveur
    client_socket.send(operation.encode('utf-8'))

    # Réception du résultat du serveur
    resultat = client_socket.recv(1024).decode('utf-8')
    print(f"Résultat de l'opération : {resultat}")

    # Fermeture de la connexion
    client_socket.close()

if __name__ == "__main__":
    client()
