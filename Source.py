import sqlite3
import pandas as pan
conn = sqlite3.connect(".\\StudentDB.sqlite")
c = conn.cursor()


def print_menu():
    print("---Main Menu---")
    print("1. Display all records")
    print("2. Create a student record")
    print("3. Update a student record")
    print("4. Delete a student record")
    print("5. Search student records")
    print("6. Exit")


def prompt_menu():
    selection = 0
    while selection != "6":
        print_menu()
        selection = input("Please enter a number: ")
        if selection == "1":
            display_all()
        elif selection == "2":
            create_student()
        elif selection == "3":
            update_student()
        elif selection == "4":
            delete_student()
        elif selection == "5":
            search_student()
        elif selection == "6":
            print("Exiting...")
        else:
            print("Invalid choice.")


def display_all():
    print(pan.read_sql_query("SELECT * from Student WHERE isDeleted = 0", conn))


def main():
    prompt_menu()
    conn.close()


def create_student():
    # add Validation ------
    print("---Create a new student record---")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    gpa = input("GPA: ")
    major = input("Major: ")
    facultyadvisor = input("Faculty advisor: ")
    c.execute("INSERT INTO Student ('FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'isDeleted') "
              "VALUES (?,?,?,?,?,?)", (fname, lname, gpa, major, facultyadvisor, 0,))
    conn.commit()
    sid = c.lastrowid
    print("Record created. Student id:", sid)
    print("Done.")


def update_student():
    print("---Update a student record---")
    sid = input("Enter a student id:")
    major = input("New major: ")
    facultyadvisor = input("New advisor: ")
    c.execute("UPDATE Student "
              "SET Major = ?, FacultyAdvisor = ? "
              "WHERE StudentID = ? AND isDeleted = 0",
              (major, facultyadvisor, sid,))
    conn.commit()


def delete_student():
    print("---Delete a student record---")
    sid = input("Enter a student id:")
    c.execute("UPDATE STUDENT "
              "SET isDeleted = 1 "
              "WHERE StudentID = ? and isDeleted = 0",
              sid)
    conn.commit()
    print("Done.")


def search_student():
    print("---Search for a student---")
    print("1. Search by Major")
    print("2. Search by GPA")
    print("3. Search by Advisor")
    print("4. Back")
    choice = input("Enter a number: ")
    if choice == "1":
        search = input("Enter the value you want to search for: ")
        query = "SELECT * FROM Student WHERE Major Like ? AND isDeleted = 0"
        print(pan.read_sql_query(query, conn, params=('%'+search+'%',)))
    elif choice == "2":
        search = input("Enter the value you want to search for: ")
        query = "SELECT * FROM Student WHERE GPA Like ? AND isDeleted = 0"
        print(pan.read_sql_query(query, conn, params=('%'+search+'%',)))
    elif choice == "3":
        search = input("Enter the value you want to search for: ")
        query = "SELECT * FROM Student WHERE FacultyAdvisor Like ? AND isDeleted = 0"
        print(pan.read_sql_query(query, conn, params=('%'+search+'%',)))
    elif choice == "4":
        pass
    else:
        print("You did not enter a valid number.")


if __name__ == "__main__":
    main()