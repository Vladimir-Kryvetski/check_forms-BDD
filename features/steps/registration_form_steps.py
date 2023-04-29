from behave import *
from selenium.webdriver.common.by import By
from locators import login_id, email_id, password_id, conf_pass_id, name_id
import re


@when('enter data: login "{login}", name "{name}", password "{password}", conf_pass "{conf_pass}", '
      'email "{email}"')
def enter_data(context, login, name, password, conf_pass, email):
    context.driver.find_element(By.ID, login_id).send_keys(login)
    context.driver.find_element(By.ID, email_id).send_keys(email)
    context.driver.find_element(By.ID, password_id).send_keys(password)
    context.driver.find_element(By.ID, conf_pass_id).send_keys(conf_pass)
    context.driver.find_element(By.ID, name_id).send_keys(name)


@when('click submit button')
def click_submit(context):
    context.driver.find_element(By.CLASS_NAME, "btn").click()


@then('the database contains: user01, dd, user01@mail.ru')
def valid_data(context):
    pattern_login = r'\buser01\b'
    pattern_name = r'\bdd\b'
    pattern_email = r'\buser01@mail.ru\b'
    match_login = re.search(pattern_login, context.db)
    match_name = re.search(pattern_name, context.db)
    match_email = re.search(pattern_email, context.db)
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
    pattern_login = r'\bwwwwww\s\s\b' #hardcode
    match = re.search(pattern_login, context.db)
    assert match is None, "login with spaces in the end is present in database"

@then('login with 5 char is not present in database')
def char5_login(context):
    pattern_login = r'\bwwwww\b' #hardcode
    match = re.search(pattern_login, context.db)
    assert match is None, "login of 5 characters is present in the database"

@when('enter data: name "{name}", password "{password}", conf_pass "{conf_pass}", email "{email}"')
def login_absent(context, name, password, conf_pass, email):
    context.driver.find_element(By.ID, email_id).send_keys(email)
    context.driver.find_element(By.ID, password_id).send_keys(password)
    context.driver.find_element(By.ID, conf_pass_id).send_keys(conf_pass)
    context.driver.find_element(By.ID, name_id).send_keys(name)


@then('empty login is not present in database')
def empty_login(context):
    pattern_login = r'\"\"' #hardcode
    match = re.search(pattern_login, context.db)
    assert match is None, "Empty login isn't present in database"

