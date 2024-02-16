import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config import paths as paths
from selenium.common.exceptions import NoSuchElementException as NEE

# Path to your WebDriver
CHROMEDRIVER_PATH = 'Dependencies/chromedriver_linux64/'

# Clean up : Screenshots of failed tests in last lap
failed_tests_screenshots = glob.glob(os.path.join(paths.SCREENSHOT_PATH, '*.png'))

for screenshots in failed_tests_screenshots:
    print("removing {}".format(screenshots))
    os.remove(screenshots)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
# Open Google.com
driver.get("https://mega.nz/login")
wait = WebDriverWait(driver, 30)  # Wait up to 30 seconds
element = wait.until(EC.visibility_of_element_located((By.ID, "login-name2")))
email_id = driver.find_element(By.ID,'login-name2')
email_id.send_keys("nsc+iosdev@mega.co.nz")
time.sleep(3)
password = driver.find_element(By.ID,'login-password2')
password.send_keys("Smart2000")
time.sleep(3)
login = driver.find_element(By.NAME,'Log in')
login.click()
# Take a screenshot
driver.save_screenshot(paths.SCREENSHOT_PATH + "/mega_login.png")
time.sleep(5)
