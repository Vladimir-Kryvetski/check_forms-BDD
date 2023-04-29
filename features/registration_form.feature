Feature: registration form checks
Background: open index page and database for all registration tests
  Given "http://hr2test.dev-bitrix.by/" page is opened
  And "database.json" is opened

Scenario: TC-1 valid login, name, password, conf_password, email
  When enter data: login "user01", name "dd", password "tests1", conf_pass "tests1", email "user01@mail.ru"
  And click submit button
  Then the database contains: user01, dd, user01@mail.ru

Scenario: TC-2  login should not contain spaces in the middle
  When  enter data: login "www  www", name "vv", password "tests1", conf_pass "tests1", email "user03@mail.ru"
  And click submit button
  Then  login with spaces in the middle is not present in database

Scenario: TC-3 login should not contain spaces in the beginning of the login
  When  enter data: login "  wwwwww", name "vv", password "tests1", conf_pass "tests1", email "user04@mail.ru"
  And click submit button
  Then  login with spaces in the begining is not present in database

Scenario: TC-4 login should not contain spaces in the end of the login
  When  enter data: login "wwwwww  ", name "vv", password "tests1", conf_pass "tests1", email "user05@mail.ru"
  And click submit button
  Then  login with spaces in the end is not present in database

Scenario: TC-5 login should be more than 5 chars
  When  enter data: login "wwwww", name "vv", password "tests1", conf_pass "tests1", email "user06@mail.ru"
  And click submit button
  Then  login with 5 char is not present in database

Scenario: TC-6 login is empty
  When  enter data: name "vv", password "tests1", conf_pass "tests1", email "user07@mail.ru"
  And click submit button
  Then  empty login is not present in database

Scenario: TC-7 password is empty
  When  enter data: login "user013", name "dg", email "user013@mail.ru"
  And click submit button
  Then  empty password is not present in database