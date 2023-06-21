# Language Python
class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero is not allowed."

# Example 
a = input("Enter the first number: ")
b = input("Enter the second number: ")
operation = input("Enter the type of operation (add, subtract, multiply, divide): ")

calculator = Calculator(a, b)

if operation == "add":
    result = calculator.add()
elif operation == "subtract":
    result = calculator.subtract()
elif operation == "multiply":
    result = calculator.multiply()
elif operation == "divide":
    result = calculator.divide()
else:
    result = "Invalid operation."

print("Result:", result)
