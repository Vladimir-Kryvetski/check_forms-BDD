from behave import *
from selenium.webdriver.common.by import By


@when('enter data: login "{login}", name "{name}", password "{password}", conf_pass "{conf_pass}", '
      'email "{email}"')
def enter_data(context, login, name, password, conf_pass, email):
    context.driver.find_element(By.ID, "login").send_keys(login)
    context.driver.find_element(By.ID, "email").send_keys(email)
    context.driver.find_element(By.ID, "pass").send_keys(password)
    context.driver.find_element(By.ID, "confirm_password").send_keys(conf_pass)
    context.driver.find_element(By.ID, "name").send_keys(name)


@when('click submit button')
def click_submit(context):
    context.driver.find_element(By.CLASS_NAME, "btn").click()


@then('the database "{database}" contains: "{login}", "{name}", "{email}"')
def validate_data(context, database, login, name, email):
    with open(database, 'r') as file:
        data = file.read()
    assert login in data and name in data and email in data


# steps for invalid data

