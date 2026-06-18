import os

import pytest
from selenium import webdriver
from utils.browser_utils import screenshots
driver= None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox", help="browser selection")



@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name=request.config.getoption("--browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)




    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        # firefox_options.add_argument("--headless")
        firefox_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Firefox(options=firefox_options)

    elif browser_name == "edge":
        reversed_options = webdriver.EdgeOptions()

        driver = webdriver.Edge(options=reversed_options)
        driver.execute_script("window.scrollBy(0, 1500);")

    # driver.execute_script("window.scrollBy(0, 1500);")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    # def add_screenshot(driver, name):
#
#     folder = "reports/screenshots"
#
#     os.makedirs(folder, exist_ok=True)
#
#     path = os.path.join(
#         folder,
#         name + ".png"
#     )
#
#     driver.save_screenshot(path)
#
#     screenshots.append(path)

#
@pytest.fixture(scope="function")
def browser_name(request):
    return request.config.getoption("--browser_name")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):

    pytest_html = item.config.pluginmanager.getplugin('html')

    outcome = yield

    report = outcome.get_result()

    extra = getattr(report, "extras", [])


    if report.when == "call":

        # Add every step screenshot
        for image in screenshots:

            html = f"""
            <div>
                <h4>{image}</h4>
                <img src="../{image}"
                width="500"
                onclick="window.open(this.src)">
            </div>
            """

            extra.append(
                pytest_html.extras.html(html)
            )


        # Failure screenshot
        if report.failed:

            failure_image = "reports/screenshots/failure.png"

            driver.save_screenshot(failure_image)

            html = f"""
            <div>
                <h4>Failure Screenshot</h4>
                <img src="../{failure_image}"
                width="500">
            </div>
            """

            extra.append(
                pytest_html.extras.html(html)
            )


        report.extras = extra