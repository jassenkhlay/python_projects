credentials = {
    "admin": "admin123",
    "teacher1": "teach2025"
}


# Dictionary to store student data
students = {}

# login system
def login():
    username = input("Enter username: ")
    password = input("Enter password: ") 

    if username in credentials:
        if credentials[username] == password:
                print(f"Login Successful. Welcome, {username}")
                return True
        else:
            print("Invalid credentials. Access Denied")
            return False
    else:
        print("Invalid Username")

# Function to calculate grade based on percentage
def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


# Add a new student
def add_student():
    roll_no = input("Enter Roll Number: ")
    if roll_no in students:
        print("Student with this roll number already exists")
        return

    name = input("Enter Student Name: ")
    marks = []

    for i in range(1, 6):
            mark = float(input(f"Enter marks for Subject {i}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
            else:
                print("Marks should be between 0 and 100.")
                break

    total = sum(marks)
    percentage = total / 5
    grade = assign_grade(percentage)

    students[roll_no] = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    print(f"Student {name} added successfully!\n")



# Search student by roll number
def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no in students:
        student = students[roll_no]
        print("Student Found:")
        print(f"Roll No: {roll_no}")
        print(f"Name   : {student['name']}")
        print(f"Marks  : {student['marks']}")
        print(f"Total  : {student['total']}")
        print(f"Percent: {student['percentage']:.2f}%")
        print(f"Grade  : {student['grade']}")
    else:
        print("Student not found")

# Display all student reports
# def display_all_students():
#     if not students:
#         print("No student records available.\n")
#         return

#     print("_______STUDENT REPORTS________")
#     print(f"{'Roll No':<10}{'Name':<20}{'Total':<10}{'Percentage':<12}{'Grade':<6}")
#     print("-" * 60)
#     print(students.keys())
#     print(students.values())
#     data = students['roll_no']
#     student = students[roll_no]
#     print(data)
#     # print(students['r'],students['name'], students['total'], students['percentage'], students['grade'])
#     print()

def display_all_students():
    print("---------------Students Data--------------------")
    print(f"{'Roll No':<10}{'Name':<20}{'Total':<10}{'Percentage':<12}{'Grade':<6}")
    for x,data in students.items():
        print(f'''|{x}     |{data['name']}   |  {data['total']} | {data['percentage']:.2f} | Grade: {data['grade']}''')


def calculate_per_marks():
    print("---------------Students Report Card--------------------")
    for x,data in students.items():
        print(f'''|{x}     |{data['name']}    | Total: {data['total']} | %: {data['percentage']:.2f} | Grade: {data['grade']}''')


# Main menu
def main_menu(): 
    while True:
        if login():
            while True:
                exit = 0
                print("====== STUDENT MANAGEMENT SYSTEM ======")
                print("1. Add Student")
                print("2. Search Student by Roll Number")
                print("3. Calculate Total Marks & Percentage")
                print("4. Display All Student Reports")
                print("5. Exit")
                
                choice = int(input("Enter your choice (1-4): "))
                
                if choice == 1:
                    add_student()
                elif choice == 2:
                    search_student()
                elif choice == 3:
                    calculate_per_marks()
                elif choice == 4:
                    display_all_students()
                elif choice == 5:
                    print("Exit")
                    cont = input("Do u want to continue?(y or n): ")
                    if cont == 'y':
                        pass
                    else:
                        print("Thanks")
                        exit = 1
                        return exit
                else:
                    print("Invalid choice. Please try again.\n")

        if exit == 1:
            print("Double Thanks")
            break

        
main_menu()
