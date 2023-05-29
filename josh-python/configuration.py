#!/usr/bin/python3

# We going to write a configuration file in three different ways. 

# updating the system 

import os 

os.system("apt-get update")
os.system("apt-get upgrade -y")
os.system("apt-get autoclean -y")
os.system("apt-get autoremove -y")

os.system("echo Systmem update and upgrade completed")

# Functions are blocks of codes that perfom a given task. 
# In programming, functions are indeed designed to perform specific actions or tasks. 
# They are blocks of code that are defined with a name and can be called or invoked when needed. Functions can accept input values called 
# arguments or parameters, and they can also return output values or perform actions without returning anything.
# By encapsulating a set of instructions within a function, you can reuse that code whenever necessary, making your program more modular and efficient. 
# Functions promote code organization, readability, and maintainability by breaking down complex tasks into smaller, manageable parts.