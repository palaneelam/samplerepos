import pytest


@pytest.fixture(scope="class")
def setup():
    print("THIS WILL BE EXECUTED FIRST IN THE BEGINNING")
    yield
    print("THIS IS THE LAST STEP OF THE TEST CASE")


@pytest.fixture(scope="class")
def dataLoad():
    print("user profile created")
    return ["Neelam", "Pal", "support@edwheel.com"]


@pytest.fixture(params=[("chrome", "Neelam"), ("firefox", "Deepti")])
def crossBrowser(request):
    return request.param
