from app.commands import Command
class SubtractCommand(Command):
    def execute(self, *args):
        try:
            numbers = list(map(float, args))  # Convert args to float and make a list
            result = numbers[0]
            for num in numbers[1:]:  # Start subtracting from the second element
                result -= num
            return result
        except ValueError:
            return "Error: All arguments must be numbers."
