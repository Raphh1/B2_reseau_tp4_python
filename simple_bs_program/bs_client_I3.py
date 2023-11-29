import socket
import re

def connect_to_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        print(f"Connecté avec succès au serveur {host} sur le port {port}")
        return s
    except socket.error:
        print("La connexion a échoué.")
        return None

def send_data_to_server(socket, user_input, pattern):
    if not isinstance(user_input, str):
        raise TypeError("La donnée envoyée au serveur doit être de type str") 

    if re.search(pattern, user_input) is None:
        raise ValueError("La donnée envoyée au serveur doit contenir le mot 'meo' ou 'waf'")

    try:
        socket.send(user_input.encode())
        data = socket.recv(1024)
        print(f"Le serveur a répondu: {data.decode()}")
    except socket.error:
        print("Erreur lors de l'envoi.")

def close_connection(socket):
    if socket:
        socket.close()
        print("Connexion fermée.")

def main():
    host = "192.168.185.4"
    port = 13337
    pattern = r"(waf|meo)"

    client_socket = connect_to_server(host, port)

    if client_socket:
        user_input = input("Que veux-tu envoyer au serveur : ")
        send_data_to_server(client_socket, user_input, pattern)
        close_connection(client_socket)

if __name__ == "__main__":
    main()
