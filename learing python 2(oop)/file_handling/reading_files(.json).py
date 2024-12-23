#hamro jason file ma hamile aage writing_file(.json).py ma haleko data bahek aaru kei explicity lekheko xa bhane khuldaina raxa
import json
#file_path = "C:/Users/CSE/OneDrive/Desktop/testpy/file_handling/test.json"
file_path = r"C:\Users\CSE\OneDrive\Desktop\testpy\file_handling.json"
with open(file_path, "r") as file:
    content = json.load(file)
    print (content)      #we can do print (content[age]) to print the age 20. i.e print(contect[key]) gives value