from behave import *
from selenium.webdriver.common.by import By
from locators import login_selector, email_selector, password_selector, conf_pass_selector, name_selector, submit_btn_xpath
import re
from selenium.common.exceptions import NoAlertPresentException


@when('enter data: login "{login}", name "{name}", password "{password}", conf_pass "{conf_pass}", '
      'email "{email}"')
def enter_data(context, login, name, password, conf_pass, email):
    context.driver.find_element(By.XPATH, login_selector).send_keys(login)
    context.driver.find_element(By.XPATH, email_selector).send_keys(email)
    context.driver.find_element(By.XPATH, password_selector).send_keys(password)
    context.driver.find_element(By.XPATH, conf_pass_selector).send_keys(conf_pass)
    context.driver.find_element(By.XPATH, name_selector).send_keys(name)


@when('click submit button')
def click_submit(context):
    context.driver.find_element(By.XPATH, submit_btn_xpath).click()
    try:
        alert = context.driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        pass

@then('the database contains: "{login}", "{name}", "{email}"')
def valid_data(context, login, name, email):
    #pattern_login = r'\buser01\b'
    #pattern_name = r'\bdd\b'
    #pattern_email = r'\buser01@mail.ru\b'
    match_login = re.search(login, context.db)
    match_name = re.search(name, context.db)
    match_email = re.search(email, context.db)
    assert match_login is not None, "valid login are not present in DB"
    assert match_name is not None, "valid name are not present in DB"
    assert match_email is not None, "valid email are not present in DB"


# negative step implementations
@then('login with spaces in the middle is not present in database')
def spaces_middle_login(context):
    pattern_login = r'\bwww\s\swww\b' #hardcode
    match = re.search(pattern_login, context.db)
    assert match is None, "login with spaces in the middle is  present in database"

@then('login with spaces in the begining is not present in database')
def spaces_begining_login(context):
    pattern_login = r'\s\s\bwwwwww\b' #hardcode
    match = re.search(pattern_login, context.db)
    assert match is None, "login with spaces in the begining is present in database"

@then('login with spaces in the end is not present in database')
def spaces_end_login(context):
    pattern_login = r'\bwwwwww\s\s' #hardcode
    match = re.search(pattern_login, context.db)
    assert match is None, "login with spaces in the end is present in database"

@then('login with 5 char is not present in database')
def char5_login(context):
    pattern_login = r'\bwwwww\b' #hardcode
    match = re.search(pattern_login, context.db)
    assert match is None, "login of 5 characters is present in the database"

@when('enter data: name "{name}", password "{password}", conf_pass "{conf_pass}", email "{email}"')
def login_absent(context, name, password, conf_pass, email):
    context.driver.find_element(By.XPATH, email_selector).send_keys(email)
    context.driver.find_element(By.XPATH, password_selector).send_keys(password)
    context.driver.find_element(By.XPATH, conf_pass_selector).send_keys(conf_pass)
    context.driver.find_element(By.XPATH, name_selector).send_keys(name)

@then('entered name - "{name}", email - "{email}" are not present in database')
def invalid_data(context, name, email):
    assert name not in context.db, "database accept invalid data"
    assert email not in context.db, "database accept invalid data"

@when('enter data: login "{login}", name "{name}", email "{email}"')
def login_absent(context, login, name, email):
    context.driver.find_element(By.XPATH, login_selector).send_keys(login)
    context.driver.find_element(By.XPATH, email_selector).send_keys(email)
    context.driver.find_element(By.XPATH, name_selector).send_keys(name)

@then('password and confirm password fields must have type password')
def check_password_type(context):
    pass_field_type = context.driver.find_element(By.XPATH, "//input[@type= 'password']")
    assert pass_field_type, "The password field is not masked."

@when('enter data: login "{login}", name "{name}", password "{password}", conf_pass "{conf_pass}"')
def empty_email(context, login, name, password, conf_pass):
    context.driver.find_element(By.XPATH, login_selector).send_keys(login)
    context.driver.find_element(By.XPATH, name_selector).send_keys(name)
    context.driver.find_element(By.XPATH, password_selector).send_keys(password)
    context.driver.find_element(By.XPATH, conf_pass_selector).send_keys(conf_pass)

@then('entered name - "{name}" is not present in database')
def check_empty_email(context, name):
    assert name not in context.db, "empty email is present in database"

@when('enter data: login "{login}", password "{password}", conf_pass "{conf_pass}", email "{email}"')
def empty_name(context, login, password, conf_pass, email):
    context.driver.find_element(By.XPATH, login_selector).send_keys(login)
    context.driver.find_element(By.XPATH, password_selector).send_keys(password)
    context.driver.find_element(By.XPATH, conf_pass_selector).send_keys(conf_pass)
    context.driver.find_element(By.XPATH, email_selector).send_keys(email)

@then('entered login - "{login}" is not present in database')
def check_empty_name(context, login):
    assert login not in context.db, "empty name is present in database"

