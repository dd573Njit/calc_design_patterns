from app.plugins.add import AddCommand
from app.plugins.greet import GreetCommand
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.exit import ExitCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

dict = {
    'greet': GreetCommand(),
    'goodbye': GoodbyeCommand(),
    "exit": ExitCommand(),
    "add": AddCommand(),
    "subtract": SubtractCommand(),
    "multiply": MultiplyCommand(),
    "divide": DivideCommand(),
}