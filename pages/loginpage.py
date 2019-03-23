from testdata.data import *
class LoginPage_1:
    def __init__(self,driver):
        self.driver=driver
        self.un="username"
        self.pwd="pwd"
        self.login="//div[text()='Login ']"
        #comment

    def enter_un(self):
        self.driver.find_element_by_id(self.un).send_keys(UN)

    def enter_pwd(self):
        self.driver.find_element_by_name(self.pwd).send_keys(PWD)

    def click_on_login(self):
        self.driver.find_element_by_xpath(self.login).click()