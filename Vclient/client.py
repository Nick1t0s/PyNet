import socket,mytools,time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65433  # The port used by the server
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    s.send("pass".encode())
    code=s.recv(1024).decode()
    code=mytools.enc(code,-2)
    s.send(code.encode())
    autotif=s.recv(1024).decode()
    if autotif == "done":
        print("done")
        s.send("name".encode())
        x=s.recv(1024).decode()
        while x != "last":
            s.send("ppp".encode())
        s.close()
        time.sleep(5)
    else:
        print(autotif)
        s.close()
#while True:
#    x=s.recv(1024)
#    print(x.decode())