#  Class for adding two numbers together
class Add:
    def __init__(self):
        self.result = 0

    def perform(self):
        nums = input("Enter numbers to add (separated by spaces): ")
        numbers = nums.split()
        numbers = [float(num) for num in numbers]
        self.result = sum(numbers)
