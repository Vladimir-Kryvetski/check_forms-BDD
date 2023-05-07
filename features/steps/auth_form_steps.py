from behave import *
from selenium.webdriver.common.by import By
from locators import login_id, email_id, password_id, conf_pass_id, name_id, submit_btn_xpath


@then('password field must have type password')
def check_password_type(context):
    pass_field_type = context.driver.find_element(By.XPATH, "//input[@type= 'password']")
    assert pass_field_type, "The password field is not masked."


@when('get list of the cookies before login')
def get_cookies_before(context):
    context.cookies_before_login = context.driver.get_cookies()


@when('enter valid: login "{login}", password "{password}"')
def enter_valid_data(context, login, password):
    context.driver.find_element(By.ID, login_id).send_keys(login)
    context.driver.find_element(By.ID, password_id).send_keys(password)

@when('get list of the cookies after login')
def get_cookies_after(context):
    context.cookies_after_login = context.driver.get_cookies()

@then('list of cookies before login and after login is not equal')
def compare_cookies(context):
    assert context.cookies_before_login != context.cookies_after_login, "user is not authorized"


@when('enter not existing: login "{login}", password "{password}"')
def enter_invalid_data(context, login, password):
    context.driver.find_element(By.ID, login_id).send_keys(login)
    context.driver.find_element(By.ID, password_id).send_keys(password)


@then('list of cookies before login and after login are equal')
def compare_cookies_not_equal(context):
    assert context.cookies_before_login == context.cookies_after_login, "user is authorized"
