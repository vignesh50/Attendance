import time

print("::: Attendance Application :::\n")
print("Description: If Student Present Enter \"p\" or enter \"a\" \n")

studentList = ['Abinaya.N','Akash.S','M.Aswin']
present = 0 
absent = 0

file_name = "DayOne.txt"
file = open(file_name,'w')

for x in studentList:
    PrtOrAbs = input(x + " is Present Today: ")

    if PrtOrAbs == "p":
        print(x + " is Present")
        present+=1
        file.write(x + " is Present\n")
    else:
        print(x + " is Absent")
        absent+=1
        file.write(x + " is Absent\n")

file.close()
print("\nFile saved Sucessfully\n")

print("\nTotal Class Present\n")
print("Today Present is: " + str(present) + " and Absent is: " + str(absent) + "\n")
time.sleep(10000)
