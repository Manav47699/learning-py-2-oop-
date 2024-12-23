#python file detection

import os                    #always import os(operating system) for file related operations

file_path = "file_handling/test.txt"   #for absolute file path, we can copy it from the file properties

if os.path.exists(file_path):
    print (f"{file_path} exists")

    if os.path.isfile(file_path):
        print ("This is a file")
    elif os.path.isdir(file_path):            #to make this condition true, keep the file in a folder and revome .txt from file path
        print ("it is a folder or directory")
else:
    print ("This file doesn't exist")