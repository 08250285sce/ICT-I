name = input("Enter your name: ")
for i in name:
    print(i)
    
li = ["Python Programming", "Python Fundamentals", "Python Interview Questions"]
for x in li: # x is a variable that takes the value od each item in the list li during each iteratio of loop
    print(x)
    
lenli = len(li) #len() returns the number of items in the list li i.e.3. the value is stored in the variable lenli.
for x in range(lenli): #x is a variable that takes the value of each index.
    print (li[x])
    
#Tuple
New_tuple = tuple(li)
for x in New_tuple:
    print(x)

lenNew_tuple = len(New_tuple)
for x in range(lenNew_tuple):
    print(New_tuple[0])

#Set
set = set(li)
for x in set:
    print(x)