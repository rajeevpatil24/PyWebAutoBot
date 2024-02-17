import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config import paths as paths
from selenium.common.exceptions import NoSuchElementException as NEE

# Path to your WebDriver
browser = "chrome"

# Clean up : Screenshots of failed tests in last lap
failed_tests_screenshots = glob.glob(os.path.join(paths.SCREENSHOT_PATH, '*.png'))

for screenshots in failed_tests_screenshots:
    print("removing {}".format(screenshots))
    os.remove(screenshots)

try:
    # Create a new instance of the Chrome driver
    # Create Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--lang=en")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    ''' Control - Headless browsing experience '''
    # opts.add_argument('--disable-gpu')

    # Initialize Chrome driver with ChromeDriverManager
    driver = Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)    
    # driver = Chrome(options=opts, executable_path=ChromeDriverManager().install())
    # driver.maximize_window()
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
    driver.quit()
except Exception as e:
    print(f"Test failed due to: {e}")
finally:
    # Close the browser
    print("In finally")
    # driver.quit()