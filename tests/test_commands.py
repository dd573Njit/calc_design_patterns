import pytest
from app import App
from command_config import dict

@pytest.fixture
def app_instance():
    """Fixture to create an app instance."""
    return App(dict)

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App(dict)
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App(dict)
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"