# 🐍 ALX Backend Python Exercises

Welcome to the **ALX Backend Python** repository!
This project contains beginner-friendly Python scripts developed as part of the ALX Software Engineering Backend Curriculum. The primary goal is to grasp foundational Python concepts through practical coding exercises.

## 📁 Repository Structure

This repository currently includes the following Python learning scripts:

| Filename                   | Description                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------- |
| `daily_reminder.py`        | A smart task reminder that prioritizes your tasks using Python `match` case logic. |
| `match_case_calculator.py` | A simple calculator using Python `match` case for basic arithmetic operations.     |
| `multiplication_table.py`  | A simple program that prints multiplication table from a certain number to another |
| `pattern_drawing.py`       | Prints a square pattern of asterisks (`*`) using nested loops.                     |
...and more!

---

## 🧠 What You'll Learn

* Python `match-case` syntax (introduced in Python 3.10+)
* Conditional logic and control flow
* Working with loops (`for`, `while`)
* Basic input/output operations
* Pattern creation using nested loops
* Error handling (e.g., division by zero)
* ...and more

---

## 🚀 Getting Started

### ✅ Prerequisites

* Python 3.10 or higher installed
* A code editor or IDE (e.g., VS Code, PyCharm)

### 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/Aalphakeem-Adroit/alx_be_python.git
cd alx_be_python
```

Then run any of the scripts using:

```bash
python3 script_name.py
```

For example:

```bash
python3 match_case_calculator.py
```

---

## 📝 File Overview

### 📌 `daily_reminder.py`

A mini daily productivity assistant.

**Features:**

* Takes task name, priority (high/medium/low), and time-bound status.
* Uses `match-case` to determine how urgent the task is and returns an appropriate message.

---

### ➕ `match_case_calculator.py`

A calculator that supports:

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`), with a check to avoid division by zero.

**Logic:**
Uses `match-case` to execute the chosen operation based on user input.

---

### 🧵 `pattern_drawing.py`

Draws a square block of asterisk (`*`) characters.

**How it works:**

* Takes the desired size as input.
* Uses a `while` loop and a nested `for` loop to print a uniform pattern.

---

## 🧪 Example Usages

**Example 1 – Task Reminder**

```
Enter your task: Submit report
Priority (high/medium/low): high
Is it time-bound? (yes/no): yes

Output: Reminder: 'Submit report' is a high priority task that requires immediate attention today!
```

**Example 2 – Calculator**

```
Enter the first number: 8
Enter the second number: 2
Choose the operation (+, -, *, /): /

Output: The result is:  4.0
```

**Example 3 – Pattern Drawing**

```
Enter the size of the pattern: 4

Output:
****
****
****
****
```

---

## 🎯 Future Plans

* Add unit tests using `unittest` or `pytest`
* Extend calculator with more operations (exponent, modulo, etc.)
* Add more beginner and intermediate-level scripts
* Create interactive menu for selecting exercises

---

## 🤝 Contributing

Contributions are welcome! If you'd like to:

* Improve the logic
* Add comments or better error handling
* Introduce new scripts

Feel free to fork this repo and submit a pull request.

---

## 📜 License

This repository is open-sourced under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

* Inspired by [ALX Software Engineering Program](https://www.alxafrica.com/)
* Thanks to the global Python community for amazing learning resources
