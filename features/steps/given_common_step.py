from selenium import webdriver
from behave import given


@given('"{index}" page is opened')
def open_index_page(context, index):
    context.driver = webdriver.Chrome()
    context.driver.get(index)


@given('"{database_path}" is opened')
def read_database(context, database_path):
    with open(database_path, 'r') as file:
        context.db = file.read()
