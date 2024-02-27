from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name, *args):
        try:
            # Execute the command with any arguments provided
            command = self.commands[command_name]
            result = command.execute(*args)  # Unpack arguments to pass to execute
            if result is not None:
                print(result)  # Or handle the command result as needed
        except KeyError:
            print(f"No such command: {command_name}")
        except Exception as e:
            print(f"Error executing command '{command_name}': {e}")