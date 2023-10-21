from math import fabs
from art import *
import os
from subprocess import call

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def clear():
    _ = call('clear' if os.name =='posix' else 'cls')

operations = {
                "+": add,
                "-": substract,
                "/": divide,
                "*": multiply
            }

def calculator():
    print(logo)
    
    keep_going = True
    first_number = float(input("Эхний тоогоо оруулна уу: "))
    for symbol in operations:
        print(symbol)

    while(keep_going):
        operation_request = input("Дээрх үйлдлээс сонгоно уу: ")
        second_number = float(input("Дараагийн тоогоо оруулна уу: "))

        #Get the desired 
        function = operations[operation_request]
        result = function(first_number, second_number)

        print(f"{first_number} {operation_request} {second_number} = {result}")
        
        choice = input(f"""Үргэлжлүүлэхийн тулд 'y' гэж оруулна уу, Шинээр эхлүүлэхийн
                        тулд 'n' гэж оруулна уу, гарахын тулд 'e' гэж оруулна уу""")

        if  choice == 'y':
            first_number = result
            clear()
        elif choice == 'n':
            calculator()
        else:
            break


calculator()