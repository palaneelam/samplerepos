import pytest


def test_firstProgram():
    print("Hi 1")

def test_firstProgram_a():
    print("Hi 2 ")

@pytest.mark.smoke
def test_firstProgram_b():
    print("Hi 3")