Feature: registration form checks

Scenario: all fields are filled with valid data
  Given "http://hr2test.dev-bitrix.by/" page is opened
  When enter valid data: login "user01", name "ss", password "tests1", conf_pass "tests1", email "user01@gmail.com"
  And click submit button
  Then valid data: user01, ss, user01@gmail.com are presence in database