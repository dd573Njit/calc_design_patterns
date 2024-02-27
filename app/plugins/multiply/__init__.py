from app.commands import Command
class MultiplyCommand(Command):
    def execute(self, *args):
        result = 1
        try:
            numbers = map(float, args)
            for i in numbers:
                result *= i
            return result
        except ValueError:
            return "Error: All arguments must be numbers."