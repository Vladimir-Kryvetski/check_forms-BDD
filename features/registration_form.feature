Feature: registration form checks
Background: open index page for all registration tests
  Given "http://hr2test.dev-bitrix.by/" page is opened

Scenario: valid login, name, password, conf_password, email
  When enter data: login "user02", name "dd", password "tests1", conf_pass "tests1", email "user02@mail.ru"
  And click submit button
  Then the database "database.json" contains: "user02", "dd", "user02@mail.ru"

Scenario: empty fields
  When click submit button
  Then login "", name "", password "", conf_pass "", email "" are not present in database