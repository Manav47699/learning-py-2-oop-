#.json file contains dictionaries 
#we have to import json module to use jason.dump() function

import json

me = {"name":"Manav Acharya",
      "age": "20",
      "facuilty":"BCT"}

file_path = r"C:\Users\CSE\OneDrive\Desktop\testpy\file_handling.json"

with open(file_path, "w") as file:
    json.dump(me, file, indent=4)         #indent na lekhda pani hunxa tio postion milako matra ho padhna sajilo hoss bhanera
    print(f"jason file was created")
