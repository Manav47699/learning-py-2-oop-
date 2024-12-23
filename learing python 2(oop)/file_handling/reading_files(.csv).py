import csv

file_path = "C:/Users/CSE/OneDrive/Desktop/testpy/file_handling/test.csv"

with open(file_path, "r") as file:
    content = csv.reader(file)
    for line in content:
        print(line)         #here print(line[0]) would give names, similarly line[1] would give ages. so the value inside the [] is for the columns  