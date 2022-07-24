from selenium.webdriver.common.by import By

class HomePageLocators(object):
    
    HOME_HEADING = (By.XPATH, "//header[@id='header']//h1")
    REGISTER_LINK = (By.LINK_TEXT, 'REGISTER')
    LOGIN_LINK = (By.LINK_TEXT, 'LOGIN')
    HOME_LINK = (By.LINK_TEXT, 'RIDES BY MJ')

class RegisterPageLocators(object):

    USERNAME_FIELD = (By.NAME, 'username')
    PASSWORD1_FIELD = (By.NAME, 'password1')
    PASSWORD2_FIELD = (By.NAME, 'password2')
    SUBMIT_BUTTON = (By.XPATH, "//div[@class='register']//section//ul[@class='actions']//input[@class='primary']")

class LoginPageLocators(object):

    USERNAME_FIELD = (By.NAME, 'username')
    PASSWORD_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, "//div[@class='login']//section//ul[@class='actions']//input[@class='primary']")
    LOGOUT_LINK = (By.LINK_TEXT, 'LOGOUT')