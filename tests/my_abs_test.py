from mock import MagicMock
from my_abs import AbstractAdder, ConcreteAdder, AddExecuter


def test_can_call_AddExecuter():
    adder = ConcreteAdder()
    AddExecuter(adder)


def test_AddExecuter_call_and_return_result():
    mock_adder = MagicMock(AbstractAdder)
    mock_adder.add = MagicMock(return_value=3)
    result = AddExecuter(mock_adder)
    mock_adder.add.assert_called_once_with(1, 2)
    assert result == 3
