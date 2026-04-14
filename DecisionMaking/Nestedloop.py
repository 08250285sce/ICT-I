#loop inside a loop

for i in range(1,4): #outer loop iterates from 1 to 3
    for j in range(i): #inner loop interst from 0 to i-1
        print(f"Outer Loop iteration {i}, inner loop iteration {j+1}")

for i in range(4): #rows #it represents the number of rows of stars to be printed. It iterates from 0 to 3, which means it will print 4 rows of stars
    for j in range(i): #colums #it represents the number of stars to be printed in each row.
        print("*", end = " ")
    print()  #end = "" for each inner loop to be printed with spacing

#Student Activity
for i in range (1,6) :
    for j in range(1, i+1):
        print(j,end = "")
    print ()

for i in range(6,0,-1):
    for i in range(i):
        print("*", end = " ")
    print()