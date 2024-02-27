from app.commands import Command


class GoodbyeCommand(Command):
    def execute(self, **kwargs):
        world = kwargs.get('world', 'World')
        bye = kwargs.get('bye', 'Goodbye')
        print(f"{bye}, {world}!")