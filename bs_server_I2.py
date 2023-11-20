import socket
from sys import exit

host = ''
port = 13337 



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
        s.bind((host, port))  
        s.listen(1)
        conn, addr = s.accept()
        print(f"Un client vient de se co et son IP c'est {addr[0]}")
except:
        print("la connexion a échoué tant pis")


while True:

    
        
    try:
        if ('meo' in data.decode("utf-8")):
            conn.sendall("Meo a toi confrere" .encode("utf-8"))
        elif ('waf' in data.decode("utf-8")):
            conn.sendall("ptdr t ki ?" .encode("utf-8"))
        else:
            conn.sendall("Mes respect humble humain" .encode("utf-8"))


        data = conn.recv(1024)

        
        if not data: break

        
        print(f"Données reçues du client : {data.decode('utf-8')}")

        
        conn.sendall("Hi mate !")

    except socket.error:
        print("Error Occured.")
        break


conn.close()

exit(0)