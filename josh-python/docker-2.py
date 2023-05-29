#!/usr/bin/python3

# Now we are going to use the os.system 

import os

def check_docker_installed():
    # Check if Docker is installed by running the docker version command
    return os.system('docker version > /dev/null 2>&1') == 0

def install_docker():
    # Update the package list and install Docker using apt
    os.system('sudo apt update')
    os.system('sudo apt install -y docker.io')

def start_docker_service():
    # Start and enable the Docker service using systemctl
    os.system('sudo systemctl start docker')
    os.system('sudo systemctl enable docker')

# Check if Docker is installed
if not check_docker_installed():
    print("Docker is not installed. Installing Docker...")
    install_docker()
    print("Docker has been installed.")
else:
    print("Docker is already installed.")

# Start and enable the Docker service
print("Starting and enabling the Docker service...")
start_docker_service()
print("Docker service has been started and enabled.")
