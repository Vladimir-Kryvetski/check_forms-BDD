Feature: general checks
Background: open register page and database
  Given "http://hr2test.dev-bitrix.by/register.php" page is opened
  And "../../htdocs/testMazurenkoMaks/database/data.json" is opened

Scenario: TC-1 check realization through form elem
  Then form element is present on the page

Scenario: TC-2 check that password encrypted
  When enter data: login "user89", name "gfgf", password "tests1", conf_pass "tests1", email "user89@mail.ru"
  And click submit button
  Then password "tests1" is not present in database
