grades = {}

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Show All")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        grades[name] = grade
        print("Student added.")
    
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in grades:
            grade = input("Enter new grade: ")
            grades[name] = grade
            print("Grade updated.")
        else:
            print("Student not found.")
    
    elif choice == "3":
        print("Student Grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade}")
    
    elif choice == "4":
        break
    
    else:
        print("Invalid choice.")
