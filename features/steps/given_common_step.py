from selenium import webdriver
from behave import given


@given('"{index}" page is opened')
def open_index_page(context, index):
    context.driver = webdriver.Chrome()
    context.driver.get(index)
