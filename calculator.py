from add import Add
from subtract import Subtract
from multiply import Multiply
from divide import Divide
from clear import Clear


class Calculator:
    def __init__(self):
        self.result = 0

    def start(self):
        while True:
            print("Add, subtract, multiply, divide, clear\n")
            choice = input("Choose an option: ")
            if choice.lower() == "add":
                add = Add()
                add.perform()
                self.result = add.result
            elif choice.lower() == "subtract":
                subtract = Subtract()
                subtract.perform()
                self.result = subtract.result
            elif choice.lower() == "multiply":
                multiply = Multiply()
                multiply.perform()
                self.result = multiply.result
            elif choice.lower() == "divide":
                divide = Divide()
                divide.perform()
                self.result = divide.result
            elif choice.lower() == "clear":
                clear = Clear()
                clear.perform()
                self.result = clear.result
            else:
                print("Invalid choice. Please try again.")
                continue

            print("Result:", self.result)
            input("Press any key to continue...")


if __name__ == '__main__':
    calculator = Calculator()
    calculator.start()
