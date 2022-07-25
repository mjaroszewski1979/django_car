from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from .locators import (
    HomePageLocators,
    RegisterPageLocators,
    LoginPageLocators, 
    CarsListPageLocators
)
import time



class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def do_login(self):
        self.do_clear(LoginPageLocators.USERNAME_FIELD)
        self.do_clear(LoginPageLocators.PASSWORD_FIELD)
        self.do_send_keys(LoginPageLocators.USERNAME_FIELD, 'testuser')
        self.do_send_keys(LoginPageLocators.PASSWORD_FIELD, '12345')
        self.do_click(LoginPageLocators.LOGIN_BUTTON)



    


class HomePage(BasePage):

    def is_title_matches(self):
        return 'My Rides | Home Page' in self.driver.title

    def is_home_heading_displayed_correctly(self):
        home_heading = self.get_element_text(HomePageLocators.HOME_HEADING)
        text = 'RIDES BY MJ'
        return text in home_heading

    def is_register_link_works(self):
        self.do_click(HomePageLocators.REGISTER_LINK)
        return 'My Rides | Register' in self.driver.title

    def is_login_link_works(self):
        self.do_click(HomePageLocators.LOGIN_LINK)
        return 'My Rides | Login' in self.driver.title

    def is_home_link_works(self):
        self.do_click(HomePageLocators.HOME_LINK)
        return 'My Rides | Home Page' in self.driver.title

class RegisterPage(BasePage):

    def is_title_matches(self):
        return 'My Rides | Register' in self.driver.title 

    def is_register_form_works(self):
        self.do_clear(RegisterPageLocators.USERNAME_FIELD)
        self.do_clear(RegisterPageLocators.PASSWORD1_FIELD)
        self.do_clear(RegisterPageLocators.PASSWORD2_FIELD)
        self.do_send_keys(RegisterPageLocators.USERNAME_FIELD, 'mjaroszewski')
        self.do_send_keys(RegisterPageLocators.PASSWORD1_FIELD, 'maciej_1245')
        self.do_send_keys(RegisterPageLocators.PASSWORD2_FIELD, 'maciej_1245')
        self.do_click(RegisterPageLocators.SUBMIT_BUTTON)
        return 'My Rides | Login' in self.driver.title 

class LoginPage(BasePage):

    def is_title_matches(self):
        return 'My Rides | Login' in self.driver.title 

    def is_login_form_works(self):
        self.do_login()
        logout_text = self.get_element_text(LoginPageLocators.LOGOUT_LINK)
        return 'LOGOUT' in logout_text

    def is_logout_link_works(self):
        self.do_click(LoginPageLocators.LOGOUT_LINK)
        return 'My Rides | Home Page' in self.driver.title

class CarsListPage(BasePage):

    def is_title_matches(self):
        return 'My Rides | Cars List' in self.driver.title 

    def is_cars_list_heading_displayed_correctly(self):
        cars_list_heading = self.get_element_text(CarsListPageLocators.CARS_LIST_HEADING)
        text = 'MY CARS'
        return text in cars_list_heading

    def is_no_cars_para_displayed_correctly(self):
        no_cars_para = self.get_element_text(CarsListPageLocators.NO_CARS_YET_PARA)
        text = 'YOU DO NOT HAVE CARS YET...'
        return text in no_cars_para

    def is_search_cars_form_works(self):
        self.do_clear(CarsListPageLocators.SEARCH_CARS_FIELD)
        self.do_send_keys(CarsListPageLocators.SEARCH_CARS_FIELD, 'porshe')
        self.do_click(CarsListPageLocators.ADD_CAR_BUTTON)
        car_list_item_text = self.get_element_text(CarsListPageLocators.CAR_LIST_ITEM)
        return 'PORSHE' in car_list_item_text

    def is_add_car_form_works(self):
        self.do_clear(CarsListPageLocators.ADD_CAR_FIELD)
        self.do_send_keys(CarsListPageLocators.ADD_CAR_FIELD, 'audi')
        self.do_click(CarsListPageLocators.ADD_CAR_SUBMIT)
        message_text = self.get_element_text(CarsListPageLocators.MESSAGE_TEXT)
        return 'ADDED AUDI TO LIST OF CARS' in message_text



    

