#file_path = r"C:\Users\CSE\OneDrive\Desktop\testpy\file_handling.txt"        #tio property bata copy garda yo path diyo ra run garda error aayo
file_path = "C:/Users/CSE/OneDrive/Desktop/testpy/file_handling/test.txt"

with open(file_path, "r") as file:
    content = file.read()
    print (content)