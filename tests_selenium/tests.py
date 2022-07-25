from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from . import page
from htmx.models import User, Car
import time




class GlobalMacroTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome('tests_selenium/chromedriver.exe')
        self.driver.set_window_size(1920, 1080)
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.car = Car.objects.create(producer='porshe')
        self.car.save()

    def tearDown(self):
        self.driver.close()


    def test_home_page(self):
        self.driver.get(self.live_server_url)
        home_page = page.HomePage(self.driver)
        assert home_page.is_title_matches()
        assert home_page.is_home_heading_displayed_correctly()
        assert home_page.is_register_link_works()
        assert home_page.is_login_link_works()

    def test_register_page(self):
        self.driver.get(self.live_server_url + reverse('register'))
        register_page = page.RegisterPage(self.driver)
        assert register_page.is_title_matches()
        assert register_page.is_register_form_works()

    def test_login_page(self):
        self.driver.get(self.live_server_url + reverse('login'))
        login_page = page.LoginPage(self.driver)
        assert login_page.is_title_matches()
        assert login_page.is_login_form_works()
        assert login_page.is_logout_link_works()

    def test_cars_list_page(self):
        self.driver.get(self.live_server_url + reverse('login'))
        cars_list_page = page.CarsListPage(self.driver)
        cars_list_page.do_login()
        self.driver.get(self.live_server_url + reverse('car_list'))
        assert cars_list_page.is_title_matches()
        assert cars_list_page.is_cars_list_heading_displayed_correctly()
        assert cars_list_page.is_no_cars_para_displayed_correctly()
        assert cars_list_page.is_search_cars_form_works()
        assert cars_list_page.is_add_car_form_works()

