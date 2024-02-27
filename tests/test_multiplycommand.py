import pytest
from app.plugins.multiply import MultiplyCommand

def test_app_multiply_command(capfd, monkeypatch, app_instance):
    """Test multiplication."""
    inputs = iter(['multiply 3 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app_instance.start()

    out, _ = capfd.readouterr()
    assert "12" in out, "The multiply command did not output the expected product."
    
def test_add_command_value_error():
    multiply_command = MultiplyCommand()
    result = multiply_command.execute("a", "b")
    assert result == "Error: All arguments must be numbers."
