# Q9. Student Marks Analyzer: 
# Store marks of multiple students in a list. 
# Using loops, calculate highest marks, lowest marks, average marks, number of students who passed, and number who failed. 
# Consider 40 as the passing mark.

# Dictionary of students with their marks in list along with subjects. For example:
students = {
     "Alice": {"English": 85, "Math": 92, "Science": 78, "History": 88, "Geography": 95},
     "Bob": {"English": 45, "Math": 50, "Science": 42, "History": 38, "Geography": 55},
     "Charlie": {"English": 90, "Math": 88, "Science": 95, "History": 82, "Geography": 78},
     "David": {"English": 30, "Math": 25, "Science": 28, "History": 35, "Geography": 40},
     "Eve": {"English": 70, "Math": 75, "Science": 80, "History": 65, "Geography": 72},
     "Frank": {"English": 55, "Math": 60, "Science": 58, "History": 52, "Geography": 48}
}

PASS_MARK = 40

def student_mark_analyser(students):
    highest_name, highest_avg = "", 0
    lowest_name, lowest_avg = "", 100
    class_total = 0
    passed = 0
    failed = 0

    for name, subjects in students.items():
        total = 0
        all_subjects_ok = True
        for subject, mark in subjects.items():
            total += mark
            if mark < PASS_MARK:
                all_subjects_ok = False

        average = total / len(subjects)
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