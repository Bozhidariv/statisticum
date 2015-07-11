from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
 
class AccountViewTest(TestCase):

    fixtures = ['users.json']

    def test_login(self):
        response = self.client.post("/accounts/login/", {})
        self.assertTrue(200, response.status_code)
        assert not response.context["user"].is_authenticated()
        
        login_successful = self.client.login(username='admin',password='admin')
        self.assertTrue(login_successful)
        

class UserProfileViewTest(TestCase):
    """Unit test for verify profile views"""
 
    fixtures = ['users.json']
 
    def setUp(self):
        login_successful  = self.client.login(username='admin',password='admin')
        self.assertTrue(login_successful)
 
    def test_profile_form_success(self):
        response = self.client.get('/profiles/edit/')
        self.assertTrue(200,response.status_code)
        self.assertTemplateUsed(response, 'profiles/edit.html')