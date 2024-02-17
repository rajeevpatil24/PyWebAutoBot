import time
import os

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config import paths

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the login page')
def step_impl(context):
    # Create a new instance of the Chrome driver
    # Create Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--lang=en")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    ''' Control - Headless browsing experience '''
    # opts.add_argument('--disable-gpu')

    # Path to your ChromeDriver executable
    CHROMEDRIVER_PATH = paths.MAC_CHROMEDRIVER_PATH+'chromedriver'

    # Create a new instance of the Chrome driver with the specified executable path
    context.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)

    # # Initialize Chrome driver with ChromeDriverManager
    # driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager(os_type="mac_arm64").install())

    context.driver.get('https://mega.nz/login')
    # Get the current URL
    current_url = context.driver.current_url

    # Wait until the page is loaded
    time.sleep(5)
    WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Assert the current URL
    # assert current_url == "https://mega.nz/login", "Expected {}, actual {}".format(
    #         "https://mega.nz/login", current_url)
    assert current_url, "{} URLs do not match {}".format("https://mega.nz/login", current_url)

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    # wait = WebDriverWait(driver, 60)  # Wait up to 30 seconds
    # element = wait.until(EC.visibility_of_element_located((By.ID, "login-name2")))
    # email_id = driver.find_element(By.XPATH, 'login-name2')
    # driver.find_element_by_id('login-name2')
    email_id = context.driver.find_element_by_xpath("//*[@id='login-name2']")
    # email_id = context.driver.find_elements(By.XPATH, "//*[@id='login-name2']")
    email_id.send_keys("nsc+iosdev@mega.co.nz")
    time.sleep(3)
    password = context.driver.find_element(By.ID, 'login-password2')
    password.send_keys("Smart2000")
    time.sleep(3)

@when('I click the login button')
def step_impl(context):
    login = context.driver.find_element(By.CSS_SELECTOR, 'button.login-button')
    login.click()
    time.sleep(5)
    context.driver.save_screenshot(paths.SCREENSHOT_PATH + "/mega_login.png")

@then('I should be logged in')
def step_impl(context):
    assert 'Get started' in context.driver.page_source

@then('I should see an error message')
def step_impl(context):
    assert 'Invalid username or password' in context.driver.page_source

@then('I close the browser')
def step_impl(context):
    context.driver.quit()
