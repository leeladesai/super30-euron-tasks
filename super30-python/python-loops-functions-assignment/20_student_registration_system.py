# Q20. Final Challenge - Student Registration System:
# Build a menu-driven application using functions + for loops + while loops.
# The system should allow users to add a student, view all students, search by ID, update student details,
# delete a student, calculate class average marks, display the highest-performing student, and exit.
# Store the records using appropriate Python data structures.

# Every student is graded on the same fixed list of subjects.
SUBJECTS = ["English", "Math", "Science", "History", "Geography"]

# students structure:
# {student_id: {"name": str, "age": int, "course": str, "marks": {subject: float}}}


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_number(prompt, cast, minimum, maximum=None):
    while True:
        try:
            value = cast(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        if value < minimum or (maximum is not None and value > maximum):
            print("Value out of range.")
            continue
        return value


def student_average(student):
    total = 0
    for mark in student["marks"].values():
        total += mark
    return total / len(student["marks"])


def print_student(student_id, student):
    print(f"ID: {student_id} | Name: {student['name']} | Age: {student['age']} | Course: {student['course']}")
    for subject, mark in student["marks"].items():
        print(f"    {subject:<10}: {mark}")
    print(f"    {'Average':<10}: {student_average(student):.2f}")


def add_student(students):
    student_id = read_text("Enter student ID : ")
    if student_id in students:
        print(f"A student with ID {student_id} already exists.")
        return
    name = read_text("Enter name : ")
    age = read_number("Enter age : ", int, 1, 120)
    course = read_text("Enter course : ")
    marks = {}
    for subject in SUBJECTS:
        marks[subject] = read_number(f"Enter {subject} marks (0-100) : ", float, 0, 100)
    students[student_id] = {"name": name, "age": age, "course": course, "marks": marks}
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students registered yet.")
        return
    for student_id, student in students.items():
        print_student(student_id, student)
        print()


def search_student(students):
    student_id = read_text("Enter student ID to search : ")
    if student_id in students:
        print_student(student_id, students[student_id])
    else:
        print(f"No student found with ID {student_id}.")


def update_student(students):
    student_id = read_text("Enter student ID to update : ")
    if student_id not in students:
        print(f"No student found with ID {student_id}.")
        return
    student = students[student_id]
    print("Current details:")
    print_student(student_id, student)
    print("Press Enter to keep the current value.")

    name = input(f"New name [{student['name']}] : ").strip()
    if name:
        student["name"] = name
    age = input(f"New age [{student['age']}] : ").strip()
    if age:
        try:
            if 1 <= int(age) <= 120:
                student["age"] = int(age)
            else:
                print("Age out of range. Keeping the old value.")
        except ValueError:
            print("Invalid age. Keeping the old value.")
    course = input(f"New course [{student['course']}] : ").strip()
    if course:
        student["course"] = course
    for subject in SUBJECTS:
        mark = input(f"New {subject} marks [{student['marks'][subject]}] : ").strip()
        if mark:
            try:
                if 0 <= float(mark) <= 100:
                    student["marks"][subject] = float(mark)
                else:
                    print("Marks out of range. Keeping the old value.")
            except ValueError:
                print("Invalid marks. Keeping the old value.")
    print("Student updated.")


def delete_student(students):
    student_id = read_text("Enter student ID to delete : ")
    if student_id in students:
        removed = students.pop(student_id)
        print(f"Deleted student {removed['name']} (ID {student_id}).")
    else:
        print(f"No student found with ID {student_id}.")


def class_average(students):
    if not students:
        print("No students registered yet.")
        return
    total = 0
    for student in students.values():
        total += student_average(student)
    print(f"Class average marks: {total / len(students):.2f}")

    print("Subject-wise class average:")
    for subject in SUBJECTS:
        subject_total = 0
        for student in students.values():
            subject_total += student["marks"][subject]
        print(f"    {subject:<10}: {subject_total / len(students):.2f}")


def top_student(students):
    if not students:
        print("No students registered yet.")
        return
    best_id = None
    for student_id, student in students.items():
        if best_id is None or student_average(student) > student_average(students[best_id]):
            best_id = student_id
    print("Highest-performing student:")
    print_student(best_id, students[best_id])


def student_registration_system():
    students = {}
    while True:
        print()
        print("===== Student Registration System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Class Average Marks")
        print("7. Highest-Performing Student")
        print("8. Exit")

        try:
            choice = input("\nEnter your choice (1-8): ")

            if choice == "1":
                add_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                class_average(students)
            elif choice == "7":
                top_student(students)
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 8.")
        except KeyboardInterrupt:
            print("\nUser interrupted the input. Exiting the program.")
            break


if __name__ == "__main__":
    student_registration_system()
