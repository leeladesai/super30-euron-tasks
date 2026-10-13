# Python Loops and Functions Assignment

- **Student Name:** Leela Desai
- **Super30 Batch:** Sep 2026

## Assignment Description

20 practice problems that build up from basic `for` loops to a complete menu-driven application:

- **Q1-Q8:** `for` loops and nested loops (number analysis, tables, sums, strings, primes, patterns)
- **Q9-Q13:** lists, dictionaries and `while` loops (marks analyzer, ATM, password retry, guessing game, calculator)
- **Q14-Q16:** functions that return values (`my_sum`, `analyze_number`, grade calculation)
- **Q17-Q19:** functions + `while` loops in small applications (shopping cart, salary calculator, bank account)
- **Q20:** final challenge, a student registration system combining functions, `for` loops and `while` loops

Each question is a separate file. The first lines of each file describe the task.

## Setup / Run Instructions

1. Install Python 3.12 or newer (the repository pins `3.12` in `.python-version`). No third-party packages are needed.
2. Open a terminal in this folder:
   ```
   cd super30-python/python-loops-functions-assignment
   ```
3. Run any program, for example:
   ```
   python3 01_number_analyzer.py
   ```
   or, with `uv` from the repository root:
   ```
   uv run super30-python/python-loops-functions-assignment/01_number_analyzer.py
   ```
4. Programs ask for input in the terminal. Press `Ctrl+C` to stop one at any time.

## Completed Questions

| # | File | What it does |
|---|---|---|
| Q1 | `01_number_analyzer.py` | Prints 1 to N, labels each even/odd, counts both |
| Q2 | `02_multiplication_table.py` | Multiplication table with a user-supplied range |
| Q3 | `03_sum_average.py` | Total and average with a loop (no `sum()`) |
| Q4 | `04_max_min.py` | Largest and smallest value with loops (no `max()`/`min()`) |
| Q5 | `05_character_frequency.py` | How many times each character occurs in a string |
| Q6 | `06_character_type_counter.py` | Counts vowels, consonants, digits, spaces and special characters |
| Q7 | `07_prime_finder.py` | Primes in a user-supplied range using nested loops |
| Q8 | `08_pattern_generator.py` | Number triangle pattern with nested `for` loops |
| Q9 | `09_student_marks_analyzer.py` | Highest, lowest, average, pass and fail counts (pass mark 40) |
| Q10 | `10_atm_simulator.py` | ATM menu with balance, deposit, withdraw and exit (starts at Rs. 10,000) |
| Q11 | `11_password_retry.py` | Three password attempts, then "Account Locked" |
| Q12 | `12_number_guessing_game.py` | Guess a number from 1 to 100 with "Too High"/"Too Low" hints |
| Q13 | `13_menu_calculator.py` | Calculator menu with division-by-zero handling |
| Q14 | `14_my_sum_function.py` | Own `my_sum(numbers)`, numbers entered by the user |
| Q15 | `15_analyze_number_function.py` | Returns sign, even/odd and prime/not prime |
| Q16 | `16_student_grade_function.py` | Marks for five named subjects, total, percentage and grade |
| Q17 | `17_shopping_cart.py` | Cart with a default item catalog and checkout |
| Q18 | `18_employee_salary.py` | Gross, tax and final salary for five employees |
| Q19 | `19_bank_account.py` | Deposit, withdraw, balance and transaction history |
| Q20 | `20_student_registration_system.py` | Add, view, search, update, delete, class average and top student |

All 20 questions are completed.

## Notes

- **Grading rules (Q16):** A is 80% and above, B 65%, C 50%, D 40%, and below 40% is Fail.
- **Salary rules (Q18):** bonus = basic x bonus%, gross = basic + bonus, tax = gross x tax%, final = gross - tax.
- **Subjects (Q9, Q16, Q20):** English, Math, Science, History and Geography.
- **Pass rule (Q9):** a student passes only if every subject is 40 or more.
- **Input handling:** the interactive programs reject invalid input and ask again instead of crashing.
