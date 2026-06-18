import json

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from utils.browser_utils import add_screenshot
from xpath import login_btn, register, username_ip, password_ip

test_data_path= 'data/data.json'
with open(test_data_path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]
@pytest.mark.parametrize("list_item",test_list)
def test_practicepage(browserInstance,browser_name,list_item):
    driver=browserInstance
    driver.get("https://practice.expandtesting.com/")
    add_screenshot(driver, "01_practice_page")

    driver.find_element(By.XPATH,login_btn).click()
    add_screenshot(driver, "02_home_page")
    driver.find_element(By.XPATH,register).click()
    add_screenshot(driver, "03_register_page")


    driver.back()

    username=driver.find_element(By.XPATH,username_ip).text
    password=driver.find_element(By.XPATH,password_ip).text

    print("username" + username)
    print("password" + password)

    assert list_item["sampleusername"] == username
    assert list_item["samplepass"] == password

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    add_screenshot(driver, "04_usernamePasswordInput")

    if browser_name=="firefox":
        driver.find_element(By.ID, "submit-login").click()

    else:
        actin=ActionChains(driver)
        actin.move_to_element(driver.find_element(By.ID, "submit-login")).click().perform()



    add_screenshot(driver, "05_after_login")

    flash_text = driver.find_element(By.ID, "flash").text
    print(flash_text)






