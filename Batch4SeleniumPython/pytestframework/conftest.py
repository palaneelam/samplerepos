import pytest


@pytest.fixture(scope="class")
def setup():
    print("\nprogram started... ")
    yield
    print("\nprogram concludes... ")


@pytest.fixture(scope="class")
def dataLoad():
    print("user profile")
    return ["Neelam", "Pal", "support@edwheel.com"]


@pytest.fixture(params=[("chrome", "palneelam", "1234"), "firefox", "edge"])
def crossBrowser(request):
    print("\nUsername")
    print("\nPassword")
    return request.param

