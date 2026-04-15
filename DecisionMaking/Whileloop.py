#while condition:
       #statement

no_of_Students = int(input("Enter the number of students: "))
i = 1 #intitialization
student_names = {} #empty dictionary to store info
while i <= no_of_Students:
    name = input("Enter the name of the student: ") #name = value
    print("The name of student {} is {}".format(i, name))
    i += 1 # i = 1+i #incrementing the value of i by 1 in each iteration of the loop
    student_names[i] = name #Student_names with the key as the value of 1

print(student_names)

while True:
    print("This is an infinite loop. Press Ctrl + C to stop it.")


#break
for i in range(4):
    if i == 2:
        break 
    print (i)
print("Loop ended")
