from behave import *
from selenium.webdriver.common.by import By
from read_database import read_database
from locators import login_id, email_id, password_id, conf_pass_id, name_id


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


@then('the database "{database}" contains: "{login}", "{name}", "{email}"')
def validate_data(context, database, login, name, email):
    data = read_database(database)
    assert login in data and name in data and email in data


# steps for invalid data

