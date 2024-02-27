from app.commands import Command


class GreetCommand(Command):
    def execute(self, **kwargs):
        name = kwargs.get('name', 'World')
        greeting = kwargs.get('greeting', 'Hello')
        print(f"{greeting}, {name}!")