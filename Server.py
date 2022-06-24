import socket
from BusinessLayer import Process


class Server:
    def __init__(self, port):
        self.host = socket.gethostname()
        self.port = port  # initiate port no above 1024
        self.server_socket = socket.socket()  # get instance
        self.server_socket.bind((self.host, self.port))  # bind host address and port together

    def Connect(self, nports):
        # configure how many client the server can listen simultaneously
        self.server_socket.listen(nports)
        conn, address = self.server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            countryName = conn.recv(1024).decode()
            if not countryName:
                # if data is not received break
                continue
            # send user's choice to business layer
            p = Process()
            jsonStr = p.getJsonStr(countryName)
            print("from connected user: " + str(countryName))
            print("jsonStr: " + jsonStr)
            conn.send(jsonStr.encode())  # send data to the client
        conn.close()  # close the connection


if __name__ == '__main__':
    server = Server(5000)
    server.Connect(2)
