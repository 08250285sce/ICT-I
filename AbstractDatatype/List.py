my_list = [1, 2, 3, "Hello", 3.14, True]
my_repeated_list = [3] * 3
print(my_list) #output: [1, 2, 3, "Hello", 3.14, True]
print(type(my_list)) #Data type of my_list is list
print(my_repeated_list) #Output: [3, 3, 3]
print(my_list[1]) #output : 2
my_list.append("World") #add element to the list
print(my_list)
my_list.extend([4, 5, 6]) #adding multiple elements to the list
print(my_list)
my_list.insert(0, "Start") #add element at a specific position of the list, index and position
print(my_list)
my_list.remove(3) #remove a particular element 
print(my_list)
my_list.pop() #removes the last element if it is not specifically given
print(my_list)
del my_list[-1]
print(my_list)
my_repeated_list.clear() #clear everything
print(my_repeated_list)
my_list[5] = False #my_list.insert(5,False) #my_list.pop(6)
print(my_list)     #d el my_list[5] #my_list.insert(5,False)
