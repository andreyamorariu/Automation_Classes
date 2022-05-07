'''
2. Scrieti cu sintaxa gherkin toate testele de la tema9 (mai putin 12).
'''
'''
Background: (la fiecare scenariu de test se fac acesti 2pasi)
Given: I am on the https://the-internet.herokuapp.com/ home page
And: I click on the Form Authentication link
'''

'''test 1
Given: I am on 'https://the-internet.herokuapp.com 'home page
When: I click Login button
Then: I land on correct page: https://the-internet.herokuapp.com/login
'''

'''test 2
Given:I am on 'https://the-internet.herokuapp.com 'home page
Then: I verify that I have the right page title "The Internet"
'''

'''test 3
Given: I am on 'https://the-internet.herokuapp.com/login' page
Then: I check if on H2 element I have "Login Page" text
'''

'''test 4
Given: I am on 'https://the-internet.herokuapp.com/login' page
Then: I verify that the Login Button is displayed
'''

'''test 5
Given: I am on 'https://the-internet.herokuapp.com/login' page
Then: I verify that the "Elemental Selenium" has the right attribute
'''

'''test 6
Given: I am on 'https://the-internet.herokuapp.com/login' page
When: I click on LogIn button
Then: I verify that error message is diplayed
'''

'''test 7
Given: I am on 'https://the-internet.herokuapp.com/login' page
When: I send keys 'abcd' for username
And: I send keys '123' for password
And: I click on LogIn button
Then: I check that error message text is "Your username is invalid!"
'''

'''test 8
Given: I am on 'https://the-internet.herokuapp.com/login' page
When: I click "x" on error message
Then: I verify that the error messsage is gone
'''

'''test 9
Given: I am on 'https://the-internet.herokuapp.com/login' page
Then: I verify that the label is Username for the Username section
Then: I verify that the label is Password for the Password section
'''

'''test 10
Given: I am on 'https://the-internet.herokuapp.com/login' page
When: I send keys "tomsmith" for username
And: I send keys "SuperSecretPassword!" for password
And: I click on Login button
And: I verify that the new URL contains "/secure"
And: I verify that the success message is displayed
Then: I verify that the success message contains "Secure area!"
'''

'''test 11
Given: I am on 'https://the-internet.herokuapp.com/login' page
When: I send keys "tomsmith" for username
And: I send keys "SuperSecretPassword!" for password
And: I click on Login button
And: I click on Logout button
Then: I check if the new url is "https://the-internet.herokuapp.com/login"
'''

