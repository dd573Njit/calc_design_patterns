import pytest
from app.plugins.add import AddCommand
def test_app_add_command(capfd, monkeypatch, app_instance):
    """Test that the REPL correctly handles the 'add' command."""
    inputs = iter(['add 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app_instance.start()

    out, _ = capfd.readouterr()
    assert "5" in out, "The add command did not output the expected sum."
    
def test_add_command_value_error():
    add_command = AddCommand()
    result = add_command.execute("a", "b")
    assert result == "Error: All arguments must be numbers."
