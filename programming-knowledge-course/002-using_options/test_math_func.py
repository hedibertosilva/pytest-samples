import math_func
import pytest
import sys


@pytest.mark.skip(reason="Skipping the test...")
def test_skipped():
    assert 1 == 1


@pytest.mark.group1
@pytest.mark.skipif(condition=sys.version_info <= (3, 7),
                    reason="Skipping because the Python version is less than 3.7.")
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(1) == 3
    assert math_func.add(0) == 2


@pytest.mark.group1
def test_product():
    assert math_func.product(7, 3) == 21
    assert math_func.product(5, 5) == 25
    assert math_func.product(2) == 4


@pytest.mark.group2
def test_add_strings():
    result = math_func.add("Hello", " World")
    assert result == "Hello World"
    assert type(result) is str
    assert 'HelloWorld' != result


@pytest.mark.group2
def test_product_strings():
    assert math_func.product("3", 3) == "333"
    result = math_func.product("Hello ", 3)
    assert result == "Hello Hello Hello "
    assert type(result) == str
    assert "Hello" in result
    assert "hello" not in result
