Feature: general checks
Background: open index page and database
  Given "http://hr2test.dev-bitrix.by/" page is opened
  And "database.json" is opened

Scenario: TC-1 check realization through form elem
  Then form element is present on the page

Scenario: TC-2 check that password encrypted
  When enter data: login "user89", name "gfgf", password "tests1", conf_pass "tests1", email "user89@mail.ru"
  And click submit button
  Then password "tests1" is not present in database

Scenario: TC-3 check that form send via AJAX
  When enter data: login "u", name "kjjkj", password "tests1", conf_pass "tests1", email "user45@mail.ru"
  And save initial url
  And click submit button
  Then the page isnt reloaded

Scenario: TC-4 check that response in JSON format
  When enter data: login "ug4", name "vbvb", password "tests1", conf_pass "tests1", email "user56@mail.ru"
  And click submit button
  Then response in json format