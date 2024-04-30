import base64

import pytest_html


def test_reserveflight(setup, request):
    setup.get("https://edwheel.com/index.php/flight-reservation-sample-page/")
    print("Ttitle is: ",setup.title)

    # setup.save_screenshot("screenshot.png")
    # screenshot_path = "screenshot.png"
    # with open(screenshot_path, "rb") as f:
    #     # Read the screenshot file
    #     screenshot_data = f.read()
    #     # Access the pytest-html plugin through the request fixture
    #     pytest_html = request.config.pluginmanager.get_plugin('html')
    #     # Add the screenshot to the HTML report
    #     pytest_html.extras.image(screenshot_data, 'Screenshot')