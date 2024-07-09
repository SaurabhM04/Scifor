# Uses concepts of pylint,flake8

import tkinter as tk
from math import sqrt

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Error: Division by zero")
    return x / y

def power(x, y):
    return x ** y

def calculate(expression):
    try:
        operators = {'+': add, '-': subtract, '*': multiply, '/': divide, '^': power}
        nums = []
        ops = []
        num = ''
        for char in expression:
            if char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    nums.append(float(num))
                    num = ''
                if char in operators:
                    ops.append(char)
                elif char == '√':
                    ops.append('√')
        if num:
            nums.append(float(num))

        while '^' in ops:
            index = ops.index('^')
            nums[index] = operators['^'](nums[index], nums[index + 1])
            del nums[index + 1]
            del ops[index]

        while '√' in ops:
            index = ops.index('√')
            nums[index] = sqrt(nums[index])
            del ops[index]

        while ops:
            num1 = nums.pop(0)
            num2 = nums.pop(0)
            op = ops.pop(0)
            result = operators[op](num1, num2)
            nums.insert(0, result)

        return nums[0]
    except Exception as e:
        return str(e)

def on_click(event):
    try:
        text = event.widget.cget("text")
        if text == "=":
            expression = entry.get()
            result = calculate(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif text == "C":
            entry.delete(0, tk.END)
        elif text == "⌫":
            current_text = entry.get()
            entry.delete(len(current_text) - 1)
        else:
            entry.insert(tk.END, text)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"Error: {str(e)}")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('⌫', 5, 0),('√', 5, 1), ('^', 5, 2), ('=', 5, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=('Arial', 20), padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_click)

root.mainloop()
