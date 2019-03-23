class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.logout="logoutLink"

    def click_on_logout(self):
        self.driver.find_element_by_id(self.logout).click()