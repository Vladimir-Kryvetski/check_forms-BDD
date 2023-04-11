from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.read_data import db


@given('"{index_page}" page is opened')
def open_index_page(context, index_page):
    context.driver = webdriver.Chrome()
    context.driver.get(index_page)


@when('enter valid data: login "{login}", name "{name}", password "{password}", conf_pass "{conf_pass}", '
      'email "{email}"')
def all_data_valid(context, login, name, password, conf_pass, email):
    context.driver.find_element(By.ID, "login").send_keys(login)
    context.driver.find_element(By.ID, "email").send_keys(email)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "confirm-password").send_keys(conf_pass)
    context.driver.find_element(By.ID, "username").send_keys(name)


@when('click submit button')
def click_submit(context):
    context.driver.find_element(By.CLASS_NAME, "btn").click()


@then('valid data: user01, ss, user01@gmail.com are presence in database')
def validate_data():
    assert "user01" in db, "user01 записан б БД"
    assert "ss" in db, "ss записан б БД"
    assert "user01@gmail.com" in db, "user01@gmail.com записан б БД"
