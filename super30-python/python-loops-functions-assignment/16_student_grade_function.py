# Q16. Student Grade Function:
# Create a function that accepts marks for five subjects, calculates total and percentage,
# and returns a grade based on rules you define such as A, B, C, D, or Fail.
# Add appropriate validation for invalid marks.

# Grading rules (percentage):
#   80 and above -> A
#   65 to 79.99  -> B
#   50 to 64.99  -> C
#   40 to 49.99  -> D
#   below 40     -> Fail

SUBJECTS = ["English", "Math", "Science", "History", "Geography"]
MAX_MARK = 100


def calculate_grade(marks):
    # marks is a dict: {subject: mark}
    for subject in SUBJECTS:
        if subject not in marks:
            raise ValueError(f"Marks for {subject} are missing.")
    if len(marks) != len(SUBJECTS):
        raise ValueError(f"Exactly {len(SUBJECTS)} subjects are required: {', '.join(SUBJECTS)}.")

    for subject, mark in marks.items():
        if mark < 0 or mark > MAX_MARK:
            raise ValueError(f"Invalid mark {mark} for {subject}. Marks must be between 0 and {MAX_MARK}.")

    total = 0
    for mark in marks.values():
        total += mark
    percentage = total / (len(SUBJECTS) * MAX_MARK) * 100

    if percentage >= 80:
        grade = "A"
    elif percentage >= 65:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    return total, percentage, grade


def read_marks():
    marks = {}
    for subject in SUBJECTS:
        while True:
            try:
                mark = float(input(f"Enter {subject} marks (0-{MAX_MARK}) : "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if mark < 0 or mark > MAX_MARK:
                print(f"Marks must be between 0 and {MAX_MARK}.")
                continue
            marks[subject] = mark
            break
    return marks


if __name__ == "__main__":
    try:
        marks = read_marks()
        total, percentage, grade = calculate_grade(marks)

        print("\n===== Marks Report =====")
        for subject, mark in marks.items():
            print(f"{subject:<10} : {mark}")
        print("-" * 22)
        print(f"Total      : {total} / {len(SUBJECTS) * MAX_MARK}")
        print(f"Percentage : {percentage:.2f}%")
        print(f"Grade      : {grade}")
    except KeyboardInterrupt:
        print("\nUser interrupted the input. Exiting the program.")
