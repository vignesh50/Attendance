file_name = "dayOne.txt"
file = open(file_name,'w')

content = input("Enter the Content: ")
file.write(content)

file.close()

print("File saved Sucessfully")

