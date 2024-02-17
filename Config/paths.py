import os

PROJECT_DIRECTORY = os.getcwd()

OUTPUT_PATH = os.path.join(PROJECT_DIRECTORY, 'output/')
SCREENSHOT_PATH = os.path.join(OUTPUT_PATH, 'screenshots/')
REPORTS_PATH = os.path.join(OUTPUT_PATH, 'reports/')

DEPENDANCIES_PATH = os.path.join(PROJECT_DIRECTORY, 'dependencies/')
MAC_CHROMEDRIVER_PATH = os.path.join(DEPENDANCIES_PATH, 'chromedriver_mac_arm64/')
CHROMEDRIVER_PATH = os.path.join(PROJECT_DIRECTORY, '')
