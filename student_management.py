import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter course: ")
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    for row in records:
        print(row)

def update_student():
    sid = input("Enter student ID to update: ")
    new_name = input("Enter new name: ")
    cursor.execute(
        "UPDATE students SET name=? WHERE id=?",
        (new_name, sid)
    )
    conn.commit()
    print("Student updated successfully!")

def delete_student():
    sid = input("Enter student ID to delete: ")
    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (sid,)
    )
    conn.commit()
    print("Student deleted successfully!")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")

conn.close()
