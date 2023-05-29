#!/usr/bin/python3

import subprocess
import shutil

def check_docker_installed():
    return shutil.which('docker') is not None

def install_docker():
    subprocess.run(['sudo', 'apt', 'update'], check=True)
    subprocess.run(['sudo', 'apt', 'install', '-y', 'docker.io'], check=True)

def start_docker_service():
    subprocess.run(['sudo', 'systemctl', 'start', 'docker'], check=True)
    subprocess.run(['sudo', 'systemctl', 'enable', 'docker'], check=True)

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

