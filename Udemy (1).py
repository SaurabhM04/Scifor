#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def display(self):
        print(self.prompt)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
        print()

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for question in self.questions:
            question.display()
            answer = input("Enter your choice (a, b, c, ...): ").strip().lower()
            if answer == question.correct_answer.lower():
                print("Correct!\n")
                self.score += 1
            else:
                print("Incorrect!\n")
        self.display_result()

    def display_result(self):
        print("Quiz Complete!")
        print(f"Your score is: {self.score} out of {len(self.questions)}")

def main():
    questions = [
        Question("What is the capital of France?", ["Paris", "London", "Rome"], "a"),
        Question("What is 2 + 2?", ["3", "4", "5"], "b"),
        Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter"], "b")
    ]

    quiz = Quiz(questions)
    print("Welcome to the Quiz!")
    input("Press Enter to start...")
    quiz.run()

if __name__ == "__main__":
    main()


# In[ ]:





# In[4]:


import math

# Encapsulation
class Shape:
    def __init__(self):
        self._name = "Shape"

    def get_name(self):
        return self._name

    def calculate_area(self):
        pass  

# Polymorphism
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self._length = length
        self._width = width
        self._name = "Rectangle"

    def calculate_area(self):
        return self._length * self._width

# Polymorphism
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._radius = radius
        self._name = "Circle"

    def calculate_area(self):
        return math.pi * self._radius ** 2

# Abstraction
class Color:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

# Multiple Inheritance
class ColoredShape(Shape, Color):
    def __init__(self, shape, color):
        Shape.__init__(self)
        Color.__init__(self, color)
        self._shape = shape

    def display_info(self):
        print(f"The {self.get_color()} {self._shape.get_name()} has area: {self._shape.calculate_area()}")

def main():
    rectangle = Rectangle(5, 4)
    circle = Circle(3)
    colored_rectangle = ColoredShape(rectangle, "blue")
    colored_circle = ColoredShape(circle, "red")

    colored_rectangle.display_info()
    colored_circle.display_info()

if __name__ == "__main__":
    main()


# In[ ]:




