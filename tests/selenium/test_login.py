import time
from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # для CI
    driver = webdriver.Chrome(options=options)

    try:
        login = LoginPage(driver)
        login.open("http://localhost:8000")
        login.login("testuser", "testpass123")
        time.sleep(1)
        driver.save_screenshot("screenshots/after_login.png")

        assert "/profile" in driver.current_url

    finally:
        driver.quit()