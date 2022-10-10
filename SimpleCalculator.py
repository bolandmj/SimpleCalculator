# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:25:36 2022

@author: maxwe
"""



print("Welcome to a Calculator!")


play = "N"   

while play != "Y":

    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    
    
    print("What operation would you like to perform?", 
                  "input '+' for addition",
                  "input '-' for subtraction",
                  "input '*' for multiplication",
                  "input '/' for division")
    
    Operation = input("> ")


    def Add():
        Total = num1 + num2
        print("{} + {} = {}".format(num1, num2, Total))
    
    def Subtract():
        Total = num1 - num2
        print("{} - {} = {}".format(num1, num2, Total))
    
    def Division():
        Total = num1 / num2
        print("{} / {} = {}".format(num1, num2, Total))
    
    def Multiply():
        Total = num1 * num2
        print("{} * {} = {}".format(num1, num2, Total))
       

    if Operation == "+":
        Add()
    elif Operation == "-":
        Subtract()
    elif Operation == "*":
        Multiply()
    elif Operation == "/":
        Division() 
    else:
        print("Not a valid operator please try again.")
        
    play = input("Would you like to end?(Y/N)")
