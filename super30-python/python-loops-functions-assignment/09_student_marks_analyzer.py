# Q9. Student Marks Analyzer: 
# Store marks of multiple students in a list. 
# Using loops, calculate highest marks, lowest marks, average marks, number of students who passed, and number who failed. 
# Consider 40 as the passing mark.

SUBJECTS = ["English", "Math", "Science", "History", "Geography"]

# List of students; each student's marks are a list in the same order as SUBJECTS.
students = [
    {"name": "Alice", "marks": [85, 92, 78, 88, 95]},
    {"name": "Bob", "marks": [45, 50, 42, 38, 55]},
    {"name": "Charlie", "marks": [90, 88, 95, 82, 78]},
    {"name": "David", "marks": [30, 25, 28, 35, 40]},
    {"name": "Eve", "marks": [70, 75, 80, 65, 72]},
    {"name": "Frank", "marks": [55, 60, 58, 52, 48]},
]

PASS_MARK = 40

def student_mark_analyser(students):
    highest_name, highest_avg = "", 0
    lowest_name, lowest_avg = "", 100
    class_total = 0
    passed = 0
    failed = 0

    for student in students:
        name = student["name"]
        marks = student["marks"]
        total = 0
        all_subjects_ok = True
        for mark in marks:
            total += mark
            if mark < PASS_MARK:
                all_subjects_ok = False

        average = total / len(marks)
        class_total += average
        print(name, "total:", total, "average:", round(average, 2))

        if average > highest_avg:
            highest_avg = average
            highest_name = name
        if average < lowest_avg:
            lowest_avg = average
            lowest_name = name

        if all_subjects_ok:
            passed += 1
        else:
            failed += 1

    print()
    print("Highest:", highest_name, round(highest_avg, 2))
    print("Lowest:", lowest_name, round(lowest_avg, 2))
    print("Class average:", round(class_total / len(students), 2))
    print("Passed:", passed)
    print("Failed:", failed)

if __name__ == "__main__":
    student_mark_analyser(students)