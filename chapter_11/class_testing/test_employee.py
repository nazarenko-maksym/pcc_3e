import pytest
from employee import Employee

@pytest.fixture
def employee():
    employee = Employee('max', 'min', 1_000_000)
    return employee

def test_give_default_raise(employee):
    """Test that default raise $5000 works."""
    employee.give_raise()
    assert 1_005_000 == employee.salary

def test_give_custom_raise(employee):
    """Test that custom raise works."""
    employee.give_raise(10_000)
    assert 1_010_000 == employee.salary
