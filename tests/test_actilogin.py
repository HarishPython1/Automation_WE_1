import time
from selenium import webdriver
import pytest
from pages.loginpage import LoginPage_1
from pages.homepage import HomePage

@pytest.fixture(scope='session')
def test_lauch_browser():
    global driver
    driver=webdriver.Chrome(executable_path="C:/Users/BTM-FAC/PycharmProjects/Automation_1/drivers/chromedriver.exe")
    driver.get("http://localhost:8097/login.do")
    driver.maximize_window()
    driver.implicitly_wait(30)

def test_login(test_lauch_browser):
    lp=LoginPage_1(driver)
    lp.enter_un()
    lp.enter_pwd()
    lp.click_on_login()

    #driver.find_element_by_id("username").send_keys("admin")
    #driver.find_element_by_name("pwd").send_keys("manager")
    #driver.find_element_by_xpath("//div[text()='Login ']").click()

def test_logout(test_lauch_browser):
    hp=HomePage(driver)
    time.sleep(5)
    hp.click_on_logout()
    #driver.find_element_by_id("logoutLink").click()

# lauch_browser()
# login()
# logout()

