#writing files (.txt, .jason, .csv)
#txt->plain text, jason->dictionary i.e "key":"value", csv->
#modes of file handling;
#w =  writes if the file already exists. clears previous data
#x = creates a file then writes
#a = append
#r = read

students =["Manav", "mausam", "himal", "madan"]

file_path = "C:/Users/CSE/OneDrive/Desktop/testpy/file_handling/test.txt"

with open(file_path, "w") as file:
    file.write("Members of our group are: \n")
    
    for student in students:
        file.write(student + "\n")      #adding anew line character
    