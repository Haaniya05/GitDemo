import os

screenshots = []

def add_screenshot(driver, name):
    folder = "reports/screenshots"

    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, name + ".png")

    print("Saving screenshot to:", path)

    driver.save_screenshot(path)

    screenshots.append(path)

    print("Current screenshots list:", screenshots)