from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.views import LogoutView


from .models import Car, UserCars, User
from . import htmx_views

class HtmxViewsTest(TestCase):

    def setUp(self):
        """
        This method is called before every test function to set up any objects
        neccessary to perform a specified task. 
        """
        self.client = Client()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.car = Car.objects.create(producer='porshe')
        self.car.save()


    def tearDown(self):
        """
        This method is called after every test function to set up any objects
        neccessary to perform a specified task. 
        """
        self.user.delete()
        self.car.delete()

    def test_check_username_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('check-username')
        self.assertEquals(resolve(url).func, htmx_views.check_username)

    def test_check_username_post_existing_username(self):
        """
        This is test method to verify if acquired response to a post request has correct status code
        and returns the expected content.
        """
        data={
            'username' : 'testuser'
        }
        response = self.client.post(reverse('check-username'), data)
        self.assertEqual(response.content, b'This username already exists')
        self.assertEqual(response.status_code, 200)

    def test_check_username_post_new_username(self):
        """
        This is test method to verify if acquired response to a post request has correct status code
        and returns the expected content.
        """
        data={
            'username' : 'newuser'
        }
        response = self.client.post(reverse('check-username'), data)
        self.assertEqual(response.content, b'This username is available')
        self.assertEqual(response.status_code, 200)

    def test_add_car_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('add_car')
        self.assertEquals(resolve(url).func, htmx_views.add_car)

    def test_add_car_post_anonymous_user(self):
        """
        This is test method to verify if acquired response to a post request has correct status code.
        """
        data = {
            'car_producer' : 'audi'
        }
        response = self.client.post(reverse('add_car'), data)
        self.assertEqual(response.status_code, 302)

    def test_add_car_post_authenticated_user(self):
        """
        This is test method to verify if acquired response to a post request made by authenticated user
        has the expected context dictionary passed to the template and returns correct status code.
        """
        data = {
            'car_producer' : 'audi'
        }
        self.client.force_login(user=self.user)
        response = self.client.post(reverse('add_car'), data)
        self.assertEqual(response.status_code, 200)
        ctx_car_producer = response.context['cars'].get()
        self.assertIsNotNone(response.context['cars'])
        self.assertEqual(ctx_car_producer.car.producer, 'audi')
        self.assertTemplateUsed(response, 'partials/car_list.html')

    def test_delete_car_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('delete_car', args= (1, ))
        self.assertEquals(resolve(url).func, htmx_views.delete_car)

    def test_delete_car_get_anonymous_user(self):
        """
        This is test method to verify if acquired response to a post request has correct status code.
        """
        response = self.client.get(reverse('delete_car', args= (1, )))
        self.assertEqual(response.status_code, 302)

    def test_delete_car_get_authenticated_user(self):
        """
        This is test method to verify if acquired response to a post request has correct status code.
        """
        data = {
            'car_producer' : 'audi'
        }
        self.client.force_login(user=self.user)
        self.client.post(reverse('add_car'), data)
        response = reverse('delete_car', args= (2, ))
        num_cars = UserCars.objects.filter(user=self.user).count()
        print(num_cars)

    

    def test_search_car_url_is_resolved(self):
        """
        This is test method to verify if appropriate view name is retrieved from a
        given url parameter.
        """
        url = reverse('search_car')
        self.assertEquals(resolve(url).func, htmx_views.search_car)

    def test_search_car_post_anonymous_user(self):
        """
        This is test method to verify if acquired response to a post request has correct status code.
        """
        data = {
            'search' : 'porshe'
        }
        response = self.client.post(reverse('search_car'), data)
        self.assertEqual(response.status_code, 302)

    def test_search_car_post_authenticated_user(self):
        """
        This is test method to verify if acquired response to a post request made by authenticated user
        has the expected context dictionary passed to the template and returns correct status code.
        """
        data = {
            'search' : 'porshe'
        }
        self.client.force_login(user=self.user)
        response = self.client.post(reverse('search_car'), data)
        self.assertEqual(response.status_code, 200)
        ctx_car_producer = response.context['results'].get()
        self.assertIsNotNone(response.context['results'])
        self.assertEqual(ctx_car_producer.producer, 'porshe')
        self.assertTemplateUsed(response, 'partials/search_results.html')


