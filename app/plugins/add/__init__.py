from app.commands import Command
class AddCommand(Command):
    def execute(self, *args):
        try:
            numbers = map(float, args)  # Convert all arguments to integers
            return sum(numbers)
        except ValueError:
            return "Error: All arguments must be numbers."