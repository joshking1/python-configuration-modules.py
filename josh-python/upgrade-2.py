#!/usr/bin/python3

# We are now going to use subprocess. 

import subprocess

def upgrade_system():
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'upgrade', '-y'])
    subprocess.run(['sudo', 'apt', 'dist-upgrade', '-y'])
    subprocess.run(['sudo', 'apt', 'autoremove', '-y'])
    subprocess.run(['sudo', 'apt', 'clean'])

def clear_cache():
    subprocess.run(['sudo', 'apt', 'clean'])

# Run the functions
print(upgrade_system())
print(clear_cache())

