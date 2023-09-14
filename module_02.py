"""
Description : Module 02 demonstration
Author : SANCHI MADAAN
Date : September 14th,2023
Usage : To demonstrate content from Module 02.
"""

# This is a single line comment 

def CalculateZ(x,y):
    x = x 
    y = y 
    z = x * y 
    return z 


answer = CalculateZ(5,6)
#print(answer)

print("Hello","World")
print("Hello","World", sep='_')
print("Hello","World", sep='_', end='$')
print("Hello","World",sep='_', end='$')

name = "John"
age = 25
print(f"My name is{name} and I am{age} years old.")

value = 3.14159
print(f"The value is {value:.2f}.")

number = 123
print(f"The number is { number :07}.")

name = "John"
print(f"Hello, {name:>10}.")

user_input=("prompt: ")

name = input("Please enter your name")
print("Name:" , name)

salary = input("Please enter your salary:")
salary = float(salary)
print(f"Salary: ${salary:,.2f}.")

standard = input("please enter your class")
print(f"CLASS: {standard:,}.")