from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    # driver = None
    print("Started . . . . . . . . . . . ")
    # # Create a new instance of the Chrome driver with Options
    # chrome_options = Options()
    # chrome_options.add_argument("--lang=en")
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--disable-notifications")

    # ''' Control - Headless browsing experience '''
    # # opts.add_argument('--disable-gpu')

    # # Initialize Chrome driver with ChromeDriverManager
    # driver = True
    # driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
    # print(dir(driver))

def after_all(context):
    driver.quit()

def after_scenario(context):
    # Take a screenshot
    driver.save_screenshot(paths.SCREENSHOT_PATH + "/mega_login.png")