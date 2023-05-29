#!/usr/bin/python3

# Let us create a folder 

import os

folder_name = "josh-python"

os.mkdir(folder_name)

# Let us now add a file inside of the folder 

file_name = "configuration.py"

path = os.path.join(folder_name,file_name)

file = open(path,"w")

content = "\n #!/usr/bin/python3"

file.write(content)

file.close()