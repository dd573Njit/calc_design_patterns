import pytest
from app.plugins.subtract import SubtractCommand

def test_app_subtract_command(capfd, monkeypatch, app_instance):
    """Test subtraction."""
    inputs = iter(['subtract 5 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app_instance.start()

    out, _ = capfd.readouterr()
    assert "3" in out, "The subtract command did not output the expected difference."
    
def test_add_command_value_error():
    subtract_command = SubtractCommand()
    result = subtract_command.execute("a", "b")
    assert result == "Error: All arguments must be numbers."