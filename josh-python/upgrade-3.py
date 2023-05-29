#!/usr/bin/python3

# subprocess.call (call is a method)   subprocess.run (is a function but for newer python) 

import subprocess

def upgrade_system():
    subprocess.call(['sudo', 'apt', 'update'])
    subprocess.call(['sudo', 'apt', 'upgrade', '-y'])
    subprocess.call(['sudo', 'apt', 'dist-upgrade', '-y'])
    subprocess.call(['sudo', 'apt', 'autoremove', '-y'])
    subprocess.call(['sudo', 'apt', 'clean'])

def clear_cache():
    subprocess.call(['sudo', 'apt', 'clean'])

# Run the functions
print(upgrade_system())
print(clear_cache())

