from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given("I open the login page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/login/")
    context.driver.save_screenshot("screenshots/step1_login_page.png")

@when("I enter valid username and password")
def step_impl(context):
    context.driver.find_element(By.NAME, "username").send_keys("testuser")
    context.driver.find_element(By.NAME, "password").send_keys("testpass123")
    context.driver.save_screenshot("screenshots/step2_credentials.png")

@when("I press the login button")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
    context.driver.save_screenshot("screenshots/step3_after_login.png")

@then("I should be redirected to the profile page")
def step_impl(context):
    assert "/profile" in context.driver.current_url
    context.driver.quit()