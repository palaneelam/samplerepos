import pytest


def test_OneProgram():
    print("This is another file!")


@pytest.mark.smoke
def test_SearchsecondProgram():
    print("This is coming from another file!")