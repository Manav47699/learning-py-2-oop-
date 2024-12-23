#csv = comma seperated values  (used mostly in excel)
# works with 2d-lists
#import csv module for 'writer'. writer acts as both a function and an object to help write csv files

import csv

students = [["name", "age", "goal"],
            ["manav", 20, "unknown"],
            ["mausam", 21, "web-develepor"]]

file_path = "C:/Users/CSE/OneDrive/Desktop/testpy/file_handling/test.csv"

with open(file_path, "w", newline="") as file:   #tio newline halena bhane row haruko bichma gap audo raxa 
    writer = csv.writer(file)
    for row in students:
        writer.writerow(row)               #writerow() is a function from csv module
    print (f"csv file was created")
