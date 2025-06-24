from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self, base_url):
        self.driver.get(f"{base_url}/login/")
        self.driver.save_screenshot("screenshots/open_login.png")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.save_screenshot("screenshots/username_filled.png")

        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.save_screenshot("screenshots/password_filled.png")

        self.driver.find_element(*self.login_button).click()
        self.driver.save_screenshot("screenshots/login_clicked.png")