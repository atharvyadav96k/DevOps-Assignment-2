run = True
while run:
    print("1)Create new file")
    print("2)Read file")
    print("3)Write to file")
    print("4)Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        filename = input("Enter the name of the new file: ")
        open(filename, "w").close()
        print(f"File '{filename}' created successfully.")
    elif(choice == 2):
        filename = input("Enter the name of the file to read: ")
        print(f"Contents of '{filename}':")
        file = open(filename, "r")
        print(file.read())
        file.close()
    elif(choice == 3):
        filename = input("Enter the name of the file to write to: ")
        content = input("Enter the content to write: ")
        file = open(filename, "a")
        file.write(content + "\n")
        file.close()
        print(f"Content written to '{filename}' successfully.")
    elif(choice == 4):
        print("Exiting the program.")
        run = False
    else:
        print("Invalid choice. Please try again.")