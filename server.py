import socket
from _thread import *
from Database import DataBase
import pickle
from PySide2.QtCore import QDateTime


DB = DataBase
DB.start_conn(DB)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ''
port = 9998
addr = (server,port)

try:
    s.bind((addr))
except socket.error as e:
    print(str(e))

s.listen(50)
print("Waiting for a connection, Server Started")


def threaded_client(conn, reply):
    print('Threaded_client: ', (reply+1))
    while True:
        try:
            choice = conn.recv(2048).decode()
            conn.send('1'.encode())
            reply = ""

            if choice== 'l':  # Login
                global datal

                #conn.send('1'.encode())
                datal = conn.recv(1024).decode()
                print(datal)
                conn.send('1'.encode())
                datap = conn.recv(1024).decode()
                print(datap)
                log_st = DB.SearchLog(DB,datal, datap)
                #print(log_st)
                if log_st == False:
                    log_st = '2'
                elif log_st == True:
                    log_st = '1'
                elif log_st == 'adm':
                    pass
                else: log_st = '2'
                conn.send(log_st.encode())
                datal=''
                datap=''
                log_st=''
                choice = ''
            elif choice == 'c':
                try:
                    print(conn.recv(1024).decode())
                    df = DB.ShowChoiseDef(DB)
                    print(df)
                    df_bytes = pickle.dumps(df)
                    conn.send(df_bytes)
                except Exception as e:
                    print('Error: ', e)
            elif choice == 'a':
                #conn.send('1'.encode())
                index = conn.recv(1024).decode()

                conn.send('1'.encode())
                data = DB.ShowDescr(DB,index)
                if data == -1:
                    conn.send('-1'.encode())
                conn.send(data.encode())
            elif choice == 'o':
                try:
                    index = conn.recv(1024).decode()

                    conn.send('1'.encode())
                    status = DB.Order(DB,index)
                    if status == '1':
                        conn.send('1'.encode())
                    else:
                        conn.send('-1'.encode())
                except Exception as e:
                    print("Error: ", e)
            conn.sendall(reply.encode())


        except Exception as e:
            #print("Error: ", e)
            break

    print("Lost connection")
    conn.close()

currentConnection = 0
while True:
    try:
        conn, addr = s.accept()
        print("Connected to:", addr)
        res = conn.recv(2048).decode()
        if res !='Connect':
            raise ValueError
        else:
            conn.sendto('1'.encode(),addr)
            start_new_thread(threaded_client, (conn, currentConnection))
            currentConnection += 1
    except Exception as e:
        print("Error: ",e)
