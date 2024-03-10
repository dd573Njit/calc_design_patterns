import os
import pkgutil
import importlib
import sys
from app.commands import CommandHandler,Command
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self, dict):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        self.dict = dict
        self.initialize_commands()
        
    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def initialize_commands(self):
        for cmd_name, cmd_instance in self.dict.items():
            self.command_handler.register_command(cmd_name, cmd_instance)
            
    def show_menu(self):
        logging.info("Available commands:")
        # List all registered commands
        for command_name in self.command_handler.commands.keys():
            logging.info(f"- {command_name}")

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")
                    
    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.dict[plugin_name] = item()
                            self.command_handler.register_command(plugin_name, item())
                            logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
        
    def start(self):
        self.load_plugins()
        self.show_menu()
        logging.info("Application started. Type 'exit' to exit.")
        while True:
            input_line = input(">>> ").strip()
            if input_line == "":
                continue  # Skip empty input
            parts = input_line.split()  # Split input into parts by whitespace
            command_name = parts[0]
            args = parts[1:]  # All the remaining parts are considered arguments

        # Check if the command is 'menu' to show available commands
            if command_name == "menu":
                self.show_menu()
                continue

            try:
                self.command_handler.execute_command(command_name, *args)
            except KeyError:
                logging.error(f"Unknown command: {command_name}")
                sys.exit(1)  # Use a non-zero exit code to indicate failure or incorrect command.

