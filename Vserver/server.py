
def inputCheckConnection():
    global clients
    conn, addr = s.accept()
    mess=conn.recv(1024)
    mess=mess.decode()
    print(mess)
    if mess == "pass":
        word=mytools.generateRandomWord()
        code=mytools.enc(word,2)
        conn.send(code.encode())
        comeCode=conn.recv(1024).decode()
        print(code)
        print(comeCode)
        if 1==1:
            print("done")
            conn.send("done".encode())
            name=conn.recv(1024).decode()
            if name in clients:
                clients[name]["lastConecting"]=mytools.getDatetimeNow()
                clients["con"]=conn
                print("i am in")
            else:
                clients[name]={"con":conn,"lastConecting":mytools.getDatetimeNow(),"commands":["do it","last"]}
                print(clients)
            if len(clients[name]["commands"])!=0:
                for i in clients[name]["commands"]:
                    if "send" in i:
                        pass
                    elif "get" in i:
                        pass
                    else:
                        print(f"compliting command {i}")
                        clients[name]["con"].send(i.encode())
                        res=clients[name]["con"].recv(1024).decode()
                        print(f"[{name.upper()}] {res}")
        else:
            print("f")
            conn.send("faling".encode())
            conn.close()

import socket,mytools,datetime
clients={}
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65433  # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
while True:
    inputCheckConnection()