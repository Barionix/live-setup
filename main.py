import os

def clone_repos():
    print("[Cloning repos...]")
    os.system("git clone https://github.com/Barionix/Trovilo")
    os.system("git clone https://github.com/Barionix/gogram")
    os.system("git clone https://github.com/Barionix/live-setup")

def set_folders():
    print("[Setting folders...]")
    os.system("cd; mkdir Office")
    clone_repos()

def install_dev_tools():
    print("[Installing git...]")
    os.system("sudo apt-get install -y git")
    print("[Installing VSCode...]")
    os.system("sudo snap install --classic code"    
def start():
    set_folders()
    install_dev_tools()

start()