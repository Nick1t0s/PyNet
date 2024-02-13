import socket
if __name__ == '__main__':
    host="www.python.org"
    adr=socket.gethostbyname(host)
    print(adr)