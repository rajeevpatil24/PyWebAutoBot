import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

# Open Google.com
driver.get("https://www.google.com")
search_pattern = driver.find_element(by='name', value="q")
search_pattern.send_keys("Narendra Modi")
time.sleep(3)
search_pattern.send_keys(Keys.ENTER)
# Take a screenshot
driver.save_screenshot(paths.SCREENSHOT_PATH + "/google_search_screenshot3.png")
time.sleep(5)
try:
    links = driver.find_element(By.CLASS_NAME,'main')
    print ("links here {}".format(links))
except NEE:
    print ("no class found")
for link in links:
    print ("please find the data here {}".format(link))
driver.quit()
