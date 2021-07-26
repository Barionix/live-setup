import os

def set_folder():
    print("[Setting folders]")
    os.system("cd; mkdir Officer")

def install_dev_tools():
    print("[Installing git]")
    os.system("sudo apt-get install -y git")
    print("[Installing VSCode]")
    os.system("sudo snap install --classic code"    
def start():
    set_folder()
    install_dev_tools()

start()