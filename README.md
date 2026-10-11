# 🧮 Python GUI Calculator

A simple and interactive **Graphical User Interface (GUI) Calculator** developed using Python and Tkinter. This project provides a button-based interface that allows users to perform basic arithmetic calculations without typing expressions directly into the terminal.

The calculator features a clean layout, number buttons, arithmetic operators, decimal support, a clear button, backspace functionality, and an equals button to calculate results.

## ✨ Features

- 🖥️ **Graphical User Interface:** Built with Python's Tkinter library.
- ➕ **Addition:** Add two or more numbers.
- ➖ **Subtraction:** Subtract numbers.
- ✖️ **Multiplication:** Multiply numbers using the `x` button.
- ➗ **Division:** Divide numbers using the `÷` button.
- 🔢 **Decimal Support:** Enter decimal numbers using the `.` button.
- ⌫ **Backspace:** Remove the last character from the current expression.
- 🧹 **Clear Button:** Reset the calculator display to `0`.
- 🟰 **Instant Results:** Calculate expressions using the equals button.
- 🎨 **Custom Interface:** Styled buttons, colors, fonts, and a dedicated display.
- 👨‍💻 **Developer Credit:** Includes a developer label in the application window.

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** — for creating the graphical user interface.
- `eval()` — for evaluating arithmetic expressions.
- Functions and event-driven programming.
- Tkinter widgets, including `Label`, `Button`, and `Frame`.
- The `grid()` and `place()` geometry managers.

## 🚀 Getting Started

### Prerequisites

Install Python 3 on your computer. Tkinter is included with many standard Python installations.

Check your Python version:

```bash
python --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Python-GUI-Calculator.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the Project Folder

```bash
cd Python-GUI-Calculator
```

### 3. Run the Calculator

If your Python file is named `main.py`, run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

A graphical calculator window should open.

**Note:** On Linux, you might need to install your distribution's Tkinter package if it is not already available.

## 🎮 How to Use

1. Launch the program.
2. Click the number buttons to enter numbers.
3. Click an arithmetic operator: `+`, `-`, `x`, or `÷`.
4. Continue entering numbers and operators to build an expression.
5. Press `=` to calculate the result.
6. Press `C` to clear the display.
7. Use `⌫` to remove the last character.
8. Use `.` to enter decimal values.

### Example Calculations

| Expression | Result |
|---|---:|
| `5+3` | `8` |
| `10-4` | `6` |
| `6x7` | `42` |
| `20÷5` | `4` |
| `2.5+1.5` | `4.0` |

## 📂 Project Structure

```text
Python-GUI-Calculator/
├── main.py
└── README.md
```

## 🧠 Concepts Practiced

This project demonstrates practical Python programming concepts:

- Creating graphical applications with Tkinter.
- Building and configuring buttons and labels.
- Connecting button clicks to callback functions.
- Updating widget properties dynamically.
- Using functions to organize application logic.
- Managing widgets with geometry managers.
- Handling arithmetic expressions and calculation errors.
- Creating an event-driven application using `mainloop()`.

## 🔮 Future Improvements

- Add keyboard support for entering numbers and operators.
- Support parentheses and more advanced mathematical operations.
- Improve expression validation and error handling.
- Prevent invalid sequences of operators and decimal points.
- Add a calculation history feature.
- Improve the layout with a modern theme.
- Add keyboard shortcuts for clear, backspace, and calculation.
- Replace `eval()` with a safer arithmetic expression parser.

## 👨‍💻 Author

Created as a Python learning project to practice Tkinter, GUI design, event-driven programming, and basic arithmetic operations.

## 📄 License

This project is intended for educational and personal learning purposes. Consider adding an MIT License if you want to allow others to use, modify, and distribute your code under its terms.
