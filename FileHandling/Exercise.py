detail = open("student.txt", "w")
detail.write("Soniya Mongar:110011\n")
detail.write("Namrata Gurung:110021\n")
detail.write("Sharmilla Ghalley:110031\n")
detail.write("Sumitra Alley:110041\n")
detail.write("Samten Dolma:110051\n")
detail.close()

print("Dummy file 'student.txt' created successfully!")


with open("student.txt", "r") as f:
    students = f.readlines()
search_name = input("Enter student name to search: ")

found = False
for line in students:
    if search_name.lower() in line.lower():  
        print("Student found")
        found = True
        break

if not found:
    print("Student not found in the file.")