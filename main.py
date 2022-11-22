class Calculator():

    def add(self, a, b):
        return a + b 

    def subtract(self, a, b):
        return a - b 

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a // b

    def clear(self):
        return 0
        
calc = Calculator()
total = 0
a = 0
b = 0
instance = 0

while True and instance == 0:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divie")
    print("5: Clear")
    print("6: Exit")

    operation = int(input("Please choose an operator: "))
    
    if operation in (1, 2, 3, 4, 5, 6):

        if (operation == 6):
            break
        
        if (operation == 5):
            total = calc.clear()
            a = calc.clear()
            b = calc.clear()
            continue

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        if operation == 1:
            total = calc.add(a, b)
            print(f"{a} + {b} = {total}")
            instance = instance + 1

        if operation == 2:
            total = calc.subtract(a, b)
            print(f"{a} - {b} = {total}")
            instance = instance + 1

        if operation == 3:
            total = calc.multiply(a, b)
            print(f"{a} * {b} = {total}")
            instance = instance + 1

        if operation == 4:
            total = calc.divide(a, b)
            print(f"{a} / {b} = {total}")
            instance = instance + 1

    else:
        print("Invalid Input")

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divie")
    print("5: Clear")
    print("6: Exit")

    operation = int(input("Please choose an operator: "))
    
    if operation in (1, 2, 3, 4, 5, 6):

        if (operation == 6):
            break
        
        if (operation == 5):
            total = calc.clear()
            a = calc.clear()
            b = calc.clear()
            continue

        a = int(input("Enter number: "))
        
        if operation == 1:
            total = calc.add(total, a)
            print(f"{total} + {a} = {total}")
            ++instance

        if operation == 2:
            total = calc.subtract(total, a)
            print(f"{total} - {a} = {total}")

        if operation == 3:
            total = calc.multiply(total, a)
            print(f"{total} * {a} = {total}")

        if operation == 4:
            total = calc.divide(total, a)
            print(f"{total} / {a} = {total}")

    else:
        print("Invalid Input")
