import socket
import pickle
from PySide2.QtCore import *



class Network:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = "localhost"
    port = 9998
    addr = (server, port)

    def connect(self):
        try:
            self.client.connect(self.addr)
            self.client.send('Connect'.encode())
            return self.client.recv(2048).decode()
        except Exception as e:
            print("Error: ", e)
            return '-1'

    def send(self, data):
        try:
            cnxn_str = (
                "DRIVER={ODBC Driver 17 for SQL Server};SERVER=CheckDot;DATABASE=CheckDotBD;UID=SA;PWD=Gfdkjrehvfy1234")
            self.client.send(data.encode())
            r = self.client.recv(2048).decode()
            if r == None:
                return -1
            return r
        except socket.error as e:
            print(e)
            return '-1'
    def send_R(self, data,status):
        if status == '1':
            try:
               self.client.send(data.encode())
               r=self.client.recv(2048).decode()
               if r == None:
                   return -1
               return (r)
            except socket.error as e:
                print(e)
                return '-1'
        else:print('Connection error')
    def recv(self):
        try:
            r=self.client.recv(2048).decode()
            if r == None:
                return -1
            return (r)
        except socket.error as e:
            print(e)
            return '-1'

    def recv_Obj(self):
        try:
            self.client.send('1'.encode())

            #print(pickle.loads(self.client.recv(4026)))
            return pickle.loads(self.client.recv(4026))
        except socket.error as e:
            print(e)
            #return '-1'
    def reconnect(self):
        try:
            self.client.close()
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.addr)
            self.client.send('Connect'.encode())
            return self.client.recv(2048).decode()
        except Exception as e:
            print("Error: ", e)
            return '-1'


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None