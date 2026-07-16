from selenium.webdriver.common.by import By


class UserIndexNav:
    def __init__(self,driver):
        self.driver = driver
        self.user_menu_dropdown = ((By.XPATH,'//*[@id="content-left"]/nav/div/ul/li[9]/a'))
        self.logout_button = ((By.XPATH, '//*[@id="content-left"]/nav/div/ul/li[9]/ul/li[3]/div/a'))

    def click_user_menu_dropdown(self):
        self.driver.find_element(*self.user_menu_dropdown).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()