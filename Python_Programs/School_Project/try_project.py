import mysql.connector as mycon
try:
    mydb = mycon.connect(host="localhost", user="root", password="1234", database="school_db")
    mycur = mydb.cursor()
except:
    print("An unexpected error occured while connecting!")

def create_db():
    # TO BE USED ONLY ONCE FOR THE CREATION OF THE DATABASE AND TABLES
    create_database = "CREATE DATABASE school_db;"
    use_database = "USE school_db;"
    
    create_table_classes = "CREATE TABLE classes(class_id INT AUTO_INCREMENT PRIMARY KEY, class_name Varchar(10) NOT NULL);"
    
    create_table_students = "CREATE TABLE students(student_id INT PRIMARY KEY, roll_number INT NOT NULL, class_id INT NOT NULL, student_name VARCHAR(100) NOT NULL, dob DATE, gender ENUM('Male', 'Female', 'Other'), FOREIGN KEY (class_id) REFERENCES classes(class_id), UNIQUE (class_id, roll_number));"
    
    create_table_exam_reports = "CREATE TABLE exam_reports (student_id INT , report_no INT, exam_name VARCHAR(100), marks_obtained INT, total_marks INT, PRIMARY KEY (student_id, report_no), FOREIGN KEY (student_id) REFERENCES students(student_id));"
    
    mycur.execute(create_database)
    mycur.execute(use_database)
    mycur.execute(create_table_classes)
    mycur.execute(create_table_students)
    mycur.execute(create_table_exam_reports)

def manage_classes():
    print("\n--- Manage Classes ---")
    print("1. Add a Class")
    print("2. View Classes")
    print("3. Delete a Class")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    match choice:
        case 1:
            class_name = input("Enter class name: ")
            query = f"INSERT INTO classes (class_name) VALUES ('{class_name}');"
            mycur.execute(query)
            print("Class added successfully.")

        case 2:
            mycur.execute("SELECT * FROM classes;")
            for row in mycur.fetchall():
                print(row)

        case 3:
            class_id = int(input("Enter class ID to delete: "))
            query = f"DELETE FROM classes WHERE class_id = {class_id};"
            mycur.execute(query)
            print("Class deleted successfully.")

        case _:
            print("Invalid choice!")

def manage_students():
    print("\n--- Manage Students ---")
    print("1. Add a Student")
    print("2. View Students")
    print("3. Delete a Student")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    match choice:
        case 1:
            student_id = int(input("Enter student ID: "))
            roll_number = int(input("Enter roll number: "))
            class_id = int(input("Enter class ID: "))
            student_name = input("Enter student name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            gender = input("Enter gender (Male/Female/Other): ")

            query = f"INSERT INTO students (student_id, roll_number, class_id, student_name, dob, gender) VALUES ({student_id}, {roll_number}, {class_id}, '{student_name}', '{dob}', '{gender}');"
            mycur.execute(query)
            print("Student added successfully.")

        case 2:
            mycur.execute("SELECT * FROM students;")
            for row in mycur.fetchall():
                print(row)

        case 3:
            student_id = int(input("Enter student ID to delete: "))
            query = f"DELETE FROM students WHERE student_id = {student_id};"
            mycur.execute(query)
            print("Student deleted successfully.")

        case _:
            print("Invalid choice!")

def manage_exam_reports():
    print("\n--- Manage Exam Reports ---")
    print("1. Add an Exam Report")
    print("2. View Exam Reports")
    print("3. Delete an Exam Report")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    match choice:
        case 1:
            student_id = int(input("Enter student ID: "))
            report_no = int(input("Enter report number: "))
            exam_name = input("Enter exam name: ")
            marks_obtained = int(input("Enter marks obtained: "))
            total_marks = int(input("Enter total marks: "))

            query = f"INSERT INTO exam_reports (student_id, report_no, exam_name, marks_obtained, total_marks) VALUES ({student_id}, {report_no}, '{exam_name}', {marks_obtained}, {total_marks});"
            mycur.execute(query)
            print("Exam report added successfully.")

        case 2:
            mycur.execute("SELECT * FROM exam_reports;")
            for row in mycur.fetchall():
                print(row)

        case 3:
            student_id = int(input("Enter student ID: "))
            report_no = int(input("Enter report number: "))
            query = f"DELETE FROM exam_reports WHERE student_id = {student_id} AND report_no = {report_no};"
            mycur.execute(query)
            print("Exam report deleted successfully.")

        case _:
            print("Invalid choice!")

def miscellaneous():
    print("\n--- Miscellaneous ---")
    print("Execute any SQL query:")
    query = input("Enter SQL query: ")

    try:
        mycur.execute(query)
        if query.strip().upper().startswith("SELECT"):
            for row in mycur.fetchall():
                print(row)
        else:
            print("query executed successfully.")
    except Exception as exception:
        print(f"An error occurred: {exception}")

def main():
    print("-------------WELCOME TO SCHOOL MANAGEMENT SYSTEM-------------")

    while True:
        print("\nSelect an option:")
        print("1. Manage Classes")
        print("2. Manage Students")
        print("3. Manage Exam Reports")
        print("4. Miscellaneous")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        match choice:
            case 1:
                manage_classes()
            case 2:
                manage_students()
            case 3:
                manage_exam_reports()
            case 4:
                miscellaneous()
            case 5:
                print("Exiting... Goodbye!")
                break
            case _:
                print("Invalid choice! Please select a valid option.")
