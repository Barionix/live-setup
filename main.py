import os

def clone_repos():
    print("[Cloning repos...]")
    os.system("git clone https://github.com/Barionix/Trovilo")
    os.system("git clone https://github.com/Barionix/gogram")
    os.system("git clone https://github.com/Barionix/live-setup")

def set_folders():
    print("[Setting folders...]")
    os.mkdir("Office")
    os.mkdir("Office/Projects") 
    os.chdir("Office/Projects")
    clone_repos()

def install_dev_tools():
    print("[Installing git...]")
    os.system("sudo apt-get install -y git")
    print("[Installing Go...]")
    os.system("sudo snap install --classic go")
    print("[Installing VSCode...]")
    os.system("sudo snap install --classic code")    

def start():
    install_dev_tools()
    set_folders()

start()
