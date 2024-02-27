from app.commands import Command
class DivideCommand(Command):
    def execute(self, *args):
        try:
            numbers = list(map(float, args))  # Convert args to float and make a list
            if len(numbers) != 2:
                return "Error: There can only be 2 arguments."
            return numbers[0] / numbers[1]
        except ValueError:
            return "Error: All arguments must be numbers."
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
