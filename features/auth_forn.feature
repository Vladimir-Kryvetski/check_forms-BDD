Feature: auth form checks
Background: open index page and database for all auth tests
  Given "http://hr2test.dev-bitrix.by/" page is opened
  And "../../htdocs/DX/database/user.json" is opened

Scenario: TC-1 Check that password crypted by dots symbols
  Then password field must have type password

Scenario: TC-2 check creating cookies + session after successful auth
  When get list of the cookies before login
  And enter valid: login "user01", password "tests1"
  And click submit button
  And get list of the cookies after login
  Then list of cookies before login and after login is not equal
  And clear cookies and cache after test

Scenario: TC-3 check valid login and not existing password
  When get list of the cookies before login
  And enter valid: login "user01", password "tests32111111"
  And click submit button
  And get list of the cookies after login
  Then list of cookies before login and after login are equal
  And clear cookies and cache after test

Scenario: TC-4 check login that is not registered in database
  When get list of the cookies before login
  And enter not existing: login "userqwe", password "tests1"
   And click submit button
  And get list of the cookies after login
  Then list of cookies before login and after login are equal
  And clear cookies and cache after test

Scenario: TC-5 check empty login
  When get list of the cookies before login
  And enter password "tests1"
   And click submit button
  And get list of the cookies after login
  Then list of cookies before login and after login are equal
  And clear cookies and cache after test

Scenario: TC-6 check invalid password
  When get list of the cookies before login
  And enter valid: login "user01", password "tes"
   And click submit button
  And get list of the cookies after login
  Then list of cookies before login and after login are equal
  And clear cookies and cache after test

Scenario: TC-7 check that word hello is present after successful login
  When enter valid: login "user01", password "tests1"
   And click submit button
  Then word hello or Hello or привет or Привет is present on the page
  And clear cookies and cache after test

Scenario: TC-8 check that all fields are necessary
  When get list of the cookies before login
  And click submit button
  And get list of the cookies after login
  Then list of cookies before login and after login are equal
  And clear cookies and cache after test