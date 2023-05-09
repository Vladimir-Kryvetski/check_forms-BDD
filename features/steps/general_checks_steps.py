from behave import *
from selenium.webdriver.common.by import By
from locators import form_elem_xpath
import json
from seleniumwire import webdriver
from seleniumwire.utils import decode as sw_decode


@then('form element is present on the page')
def check_form_presence(context):
    form_elem = context.driver.find_element(By.XPATH, form_elem_xpath)
    try:
        assert form_elem is not None
    except NoSuchElementException:
        assert False, "form element is missing"

@then('password "{password}" is not present in database')
def check_encryption(context, password):
    assert password not in context.db, "password isn't encrypted"

@when('save initial url')
def save_init_url(context):
    context.intit_url = context.driver.current_url

@then('the page isnt reloaded')
def check_ajax(context):
    assert context.driver.current_url == context.intit_url, "request is sent without AJAX"

@then('response in json format')
def check_json_response(context):

