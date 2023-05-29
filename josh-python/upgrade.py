#!/usr/bin/python3 

# We are going to do this using the functions 

import os 

def upgrade_system():
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')
    os.system('sudo apt dist-upgrade -y')
    os.system('sudo apt autoremove -y')
    os.system('sudo apt clean')

def clear_cache():
    os.system("apt-get autoclean -y")

# Let us now call the function to do the job 
print(upgrade_system())
print(clear_cache())
