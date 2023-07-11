Feature: registration form checks
Background: open index page and database for all registration tests
  Given "http://hr2test.dev-bitrix.by/registr" page is opened
  And "../../htdocs/DX/database/user.json" is opened

Scenario: TC-1 valid login, name, password, conf_password, email
  When enter data: login "user01", name "dd", password "tests1", conf_pass "tests1", email "user01@mail.ru"
  And click submit button
  Then the database contains: "user01", "dd", "user01@mail.ru"

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

Scenario: TC-6 login contains only spaces
  When  enter data: login "      ", name "abc", password "tests1", conf_pass "tests1", email "user07@mail.ru"
  And click submit button
  Then  entered name - "abc", email - "user07@mail.ru" are not present in database

Scenario: TC-7 password is empty
  When  enter data: login "user100", name "qwe", email "user100@mail.ru"
  And click submit button
  Then  entered name - "qwe", email - "user100@mail.ru" are not present in database

Scenario: TC-8 Check that password crypted by dots symbols
  Then password and confirm password fields must have type password

Scenario: TC-9 Check the length of the password
  When enter data: login "user101", name "rty", password "test1", conf_pass "test1", email "user101@mail.ru"
  And click submit button
  Then entered name - "rty", email - "user101@mail.ru" are not present in database

Scenario: TC-10 Check that password only with numbers is not accepted
  When enter data: login "user102", name "uio", password "123456", conf_pass "123456", email "user102@mail.ru"
  And click submit button
  Then entered name - "uio", email - "user102@mail.ru" are not present in database

Scenario: TC-11 Check that password only with letters is not accepted
  When enter data: login "user103", name "asdd", password "testss", conf_pass "testss", email "user103@mail.ru"
  And click submit button
  Then entered name - "asdd", email - "user103@mail.ru" are not present in database

Scenario: TC-12 Check that password with spaces in the middle of the password is not accepted
  When enter data: login "user104", name "fghh", password "tes ts1", conf_pass "tes ts1", email "user104@mail.ru"
  And click submit button
  Then entered name - "fghh", email - "user104@mail.ru" are not present in database

Scenario: TC-13 Check that password with spaces in the beginning of the password is not accepted
  When enter data: login "user105", name "jkll", password "  tests1", conf_pass "  tests1", email "user105@mail.ru"
  And click submit button
  Then entered name - "jkll", email - "user105@mail.ru" are not present in database

Scenario: TC-14 Check that password with spaces in the beginning of the password is not accepted
  When enter data: login "user106", name "zxcc", password "tests1  ", conf_pass "tests1  ", email "user106@mail.ru"
  And click submit button
  Then entered name - "zxcc", email - "user106@mail.ru" are not present in database

Scenario: TC-15 Check that password with special symbols is not accepted
  When enter data: login "user107", name "vbnn", password "tests1@", conf_pass "tests1@", email "user107@mail.ru"
  And click submit button
  Then entered name - "vbnn", email - "user107@mail.ru" are not present in database

Scenario: TC-16 Check that password that contains only spaces is not accepted
  When enter data: login "user108", name "nmmm", password "      ", conf_pass "      ", email "user108@mail.ru"
  And click submit button
  Then entered name - "nmmm", email - "user108@mail.ru" are not present in database

Scenario: TC-17 Check that password is not accepted if it doesn't match with confirm password
  When enter data: login "user109", name "qwww", password "tests1", conf_pass "tests2", email "user109@mail.ru"
  And click submit button
  Then entered name - "qwww", email - "user109@mail.ru" are not present in database

Scenario: TC-18 Check empty email
  When enter data: login "user110", name "weee", password "tests1", conf_pass "tests1"
  And click submit button
  Then entered name - "weee" is not present in database

Scenario: TC-20 Check email with @@
  When enter data: login "user111", name "errr", password "tests1", conf_pass "tests1", email "user111@@mail.ru"
  And click submit button
  Then entered name - "errr" is not present in database

Scenario: TC-21 Check email with spaces in the middle
  When enter data: login "user112", name "rttt", password "tests1", conf_pass "tests1", email "user 112@@mail.ru"
  And click submit button
  Then entered name - "rttt" is not present in database

Scenario: TC-22 Check email without domain part @admin
  When enter data: login "user113", name "tyyy", password "tests1", conf_pass "tests1", email "user113mail.ru"
  And click submit button
  Then entered name - "tyyy" is not present in database

Scenario: TC-23 Check email without dot (admin@mailru)
  When enter data: login "user114", name "yuuu", password "tests1", conf_pass "tests1", email "user114@mailru"
  And click submit button
  Then entered name - "yuuu" is not present in database

Scenario: TC-24 Check email that has been already registered
  When enter data: login "user115", name "uiii", password "tests1", conf_pass "tests1", email "user01@mail.ru"
  And click submit button
  Then entered name - "uiii" is not present in database

Scenario: TC-25 Check empty name
  When enter data: login "user116", password "tests1", conf_pass "tests1", email "user116mail.ru"
  And click submit button
  Then entered login - "user116" is not present in database

Scenario: TC-26 Check min length of the name 2 chars
  When enter data: login "user117", name "n", password "tests1", conf_pass "tests1", email "user117@mail.ru"
  And click submit button
  Then entered login - "user117" is not present in database

Scenario: TC-27 Check name with spaces in the middle
  When enter data: login "user118", name "op pp", password "tests1", conf_pass "tests1", email "user118@mail.ru"
  And click submit button
  Then entered login - "user118" is not present in database

Scenario: TC-28 Check name with spaces in the beginning
  When enter data: login "user119", name "  asss", password "tests1", conf_pass "tests1", email "user119@mail.ru"
  And click submit button
  Then entered login - "user119" is not present in database

Scenario: TC-29 Check name with spaces in the end
  When enter data: login "user120", name "sddd  ", password "tests1", conf_pass "tests1", email "user120@mail.ru"
  And click submit button
  Then entered login - "user120" is not present in database

Scenario: TC-30 Check name contain only spaces
  When enter data: login "user121", name "     ", password "tests1", conf_pass "tests1", email "user121@mail.ru"
  And click submit button
  Then entered login - "user121" is not present in database