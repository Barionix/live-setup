import os

git = "sudo apt-get install -y code"
vscode = "sudo snap install --classic code"


def set_folder():
    print("[Setting folders]")
    os.system("cd; mkdir Officer")

def start():
    set_folder()

start()