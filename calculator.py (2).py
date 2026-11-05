#!/usr/bin/env python
# coding: utf-8

# In[10]:


#python calculator

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+,-,*,/): ")

    if op =="+":
        print("Addition:", num1 + num2)
    elif op == "-":
        print("substraction:", num1 - num2)
    elif op =="*":
        result = num1 * num2
        print("Multiplication:", result)
    elif op =="/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print("Division:", result)
    else:
        print("Invalid operation")

    choice = input("Enter 8 to exit or any other key to continue: ")

    if choice == "8":
        print("Calculator closed!")
        break



# In[ ]:




