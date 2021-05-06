import socket


class Client_one:
    def client_one(self):
        HOST = socket.gethostname()
        PORT = 1298
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        name = "Slave1"
        while True:
            line = (str(sock.recv(1024), 'utf-8'))
            if (line.startswith("name?")):
                sock.send(bytes(name, 'utf-8'))
            elif(line.startswith("msg?")):
                print(line[4:])
            # if(name.startswith("master")):
            #     msg = input("Enter a message >>>> ")
            #     sock.sendall(bytes("msg?"+msg, 'utf-8'))


Client_one().client_one()
