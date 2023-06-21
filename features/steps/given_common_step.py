from selenium import webdriver
from behave import given
from selenium.webdriver.chrome.options import Options

#creating of instance webdriver with options to launch chrome without errors on server
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')


@given('"{index}" page is opened')
def open_index_page(context, index):
    context.driver = webdriver.Chrome(options = chrome_options, executable_path = '/home/hdd/hr2test/behaveTests/chromedriver')
    context.driver.get(index)


@given('"{database_path}" is opened')
def read_database(context, database_path):
    with open(database_path, 'r') as file:
        context.db = file.read()
