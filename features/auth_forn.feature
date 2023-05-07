Feature: auth form checks
Background: open index page and database for all auth tests
  Given "http://hr2test.dev-bitrix.by/login.html" page is opened
  And "database.json" is opened

Scenario: TC-1 Check that password crypted by dots symbols
  Then password field must have type password

Scenario: TC-2 check creating cookies + session after successful auth
  When get list of the cookies before login
  And enter valid: login "user01", password "tests1"
  And click submit button
  And get list of the cookies after login
  Then list of cookies before login and after login is not equal

Scenario: TC-3 check valid login and invalid password
  When get list of the cookies before login
  And enter valid: login "user01", password "tests321"
   And click submit button
  And get list of the cookies after login
  Then list of cookies before login and after login is not equal

Scenario: TC-4 check login that is not registered in database
  When get list of the cookies before login
  And enter not existing: login "userqwe", password "tests1"
   And click submit button
  And get list of the cookies after login
  Then list of cookies before login and after login are equal