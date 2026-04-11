import pytest
from src.habits import add_habit, complete_habit


def test_add_habit_valid():
    add_habit("Estudar Python")
    assert True


def test_add_habit_invalid():
    with pytest.raises(ValueError):
        add_habit("")


def test_complete_invalid_index():
    with pytest.raises(IndexError):
        complete_habit(999)