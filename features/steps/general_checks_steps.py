from behave import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@then('form element is present on the page')
def check_form_presence(context):
    try:
        context.driver.find_element(By.TAG_NAME, 'form')
    except NoSuchElementException:
        assert False, "Элемент <form> не найден на странице"

@then('password "{password}" is not present in database')
def check_encryption(context, password):
    assert password not in context.db, "password isn't encrypted"




