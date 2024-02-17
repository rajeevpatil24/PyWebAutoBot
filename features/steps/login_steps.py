from behave import given, when, then
from selenium import webdriver

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://mega.nz/login')

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    wait = WebDriverWait(driver, 60)  # Wait up to 30 seconds
    element = wait.until(EC.visibility_of_element_located((By.ID, "login-name2")))
    email_id = driver.find_element(By.ID, 'login-name2')
    email_id.send_keys("nsc+iosdev@mega.co.nz")
    time.sleep(3)
    password = driver.find_element(By.ID, 'login-password2')
    password.send_keys("Smart2000")
    time.sleep(10)

@when('I click the login button')
def step_impl(context):
    login = driver.find_element(By.NAME, 'Log in')
    login.click()

@then('I should be logged in')
def step_impl(context):
    assert 'Welcome' in context.driver.page_source

@then('I should see an error message')
def step_impl(context):
    assert 'Invalid username or password' in context.driver.page_source

@then('I close the browser')
def step_impl(context):
    context.driver.quit()
