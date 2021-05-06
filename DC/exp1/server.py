import socket


def server():
    HOST = socket.gethostname()
    PORT = 1298
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)
    con, client_address = sock.accept()
    while True:
        data = str(con.recv(1024), 'utf-8')
        if(data == "bye"):
            print("Client Left.\nBye !!\nEnd.")
            break
        else:
            val = 0
            data = data.split(" ")
            if(int(data[1]) == 1):
                val = int(data[0]) + int(data[2])
                print(f"{data[0]} + {data[2]} = {val}")
                val = f"Server >>> {data[0]} + {data[2]} = {val}"
            elif(int(data[1]) == 2):
                val = int(data[0]) - int(data[2])
                print(f"{data[0]} - {data[2]} = {val}")
                val = f"Server >>> {data[0]} - {data[2]} = {val}"
            elif(int(data[1]) == 3):
                val = int(data[0]) * int(data[2])
                print(f"{data[0]} * {data[2]} = {val}")
                val = f"Server >>> {data[0]} * {data[2]} = {val}"
            elif(int(data[1]) == 4):
                val = int(data[0]) / int(data[2])
                print(f"{data[0]} / {data[2]} = {val}")
                val = f"Server >>> {data[0]} / {data[2]} = {val}"
            elif(int(data[1]) == 5):
                val = int(data[0]) % int(data[2])
                print(f"{data[0]} % {data[2]} = {val}")
                val = f"Server >>> {data[0]} % {data[2]} = {val}"
            con.send(bytes(str(val), 'utf-8'))
    con.close()


if __name__ == '__main__':
    server()
