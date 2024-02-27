import pytest
from app.plugins.divide import DivideCommand

def test_app_divide_command(capfd, monkeypatch, app_instance):
    """Test division."""
    inputs = iter(['divide 8 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app_instance.start()

    out, _ = capfd.readouterr()
    assert "4" in out, "The divide command did not output the expected quotient."
    
def test_divide_command_value_error():
    divide_command = DivideCommand()
    result = divide_command.execute("a", "b")
    assert result == "Error: All arguments must be numbers."
    
def test_divide_command_correct_argument_count():
    divide_command = DivideCommand()
    result = divide_command.execute("10", "2")
    assert result == 5.0  # Assuming successful division returns a float

def test_divide_command_incorrect_argument_count():
    divide_command = DivideCommand()
    result = divide_command.execute("10", "2", "3")  # Too many arguments
    assert result == "Error: There can only be 2 arguments."
    
def test_app_divide_by_zero_command(capfd, monkeypatch, app_instance):
    """Test that the REPL correctly handles a divide by zero attempt."""
    inputs = iter(['divide 10 0', 'exit'])  # Input leading to divide by zero
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app_instance.start()

    out, _ = capfd.readouterr()
    # Assuming your DivideCommand outputs a specific error message for divide by zero
    expected_error_message = "Error: Cannot divide by zero."  # Adjust based on your actual error message
    assert expected_error_message in out, "The divide command did not handle divide by zero as expected."