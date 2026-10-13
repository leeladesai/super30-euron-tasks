# Q18. Employee Salary Calculator:
# Create a function that accepts employee name, basic salary, bonus percentage, and tax percentage.
# Calculate gross salary, tax amount, and final salary.
# Process at least five employees using a loop.

# Rules: bonus = basic * bonus% | gross = basic + bonus | tax = gross * tax% | final = gross - tax

NUM_EMPLOYEES = 5


def calculate_salary(name, basic_salary, bonus_percent, tax_percent):
    bonus = basic_salary * bonus_percent / 100
    gross_salary = basic_salary + bonus
    tax_amount = gross_salary * tax_percent / 100
    final_salary = gross_salary - tax_amount
    return {
        "name": name,
        "basic": basic_salary,
        "gross": gross_salary,
        "tax": tax_amount,
        "final": final_salary,
    }


def read_number(prompt, minimum, maximum=None):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if value < minimum or (maximum is not None and value > maximum):
            limit = f"{minimum} to {maximum}" if maximum is not None else f"{minimum} or more"
            print(f"Value must be {limit}.")
            continue
        return value


def main():
    results = []
    for i in range(1, NUM_EMPLOYEES + 1):
        print(f"\n--- Employee {i} of {NUM_EMPLOYEES} ---")
        name = input("Enter employee name : ").strip() or f"Employee {i}"
        basic = read_number("Enter basic salary : ", 0)
        bonus_percent = read_number("Enter bonus percentage (0-100) : ", 0, 100)
        tax_percent = read_number("Enter tax percentage (0-100) : ", 0, 100)
        results.append(calculate_salary(name, basic, bonus_percent, tax_percent))

    print("\n===== Salary Report =====")
    print(f"{'Name':<15}{'Basic':>12}{'Gross':>12}{'Tax':>12}{'Final':>12}")
    print("-" * 63)
    for r in results:
        print(f"{r['name']:<15}{r['basic']:>12.2f}{r['gross']:>12.2f}{r['tax']:>12.2f}{r['final']:>12.2f}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nUser interrupted the input. Exiting the program.")
