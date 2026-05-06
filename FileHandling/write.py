newFile = open("newFile.txt", "w")
print(newFile)

newFile.write("This is a new file created by python.")
newFile.close()

FileOverwrite = open("newFile.txt", "w")
FileOverwrite.write("The contents of the newFile is now changed.")
FileOverwrite.close()
