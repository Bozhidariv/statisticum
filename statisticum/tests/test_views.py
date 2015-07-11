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


class ViewsRestictionsTest(TestCase):

    def check_restriction(self,url,template):
        response = self.client.get(url,follow=True)
        self.assertTrue(200, response.status_code)
        assert not response.context["user"].is_authenticated()
        self.assertTemplateNotUsed(response, template)


    def test_profile(self):
        self.check_restriction('/profiles/edit/','profiles/edit.html')


    def test_game(self):
        self.check_restriction('/games/','games/index.html')   


    def test_game_wins(self):
        self.check_restriction('/games/wins/','games/wins.html')


    def test_game_losts(self):
        self.check_restriction('/games/losts/','games/losts.html')


    def test_game_draws(self):
        self.check_restriction('/games/draws/','games/draws.html')

class ViewsRenderingTest(TestCase):

    fixtures = ['users.json']

    def setUp(self):
        login_successful  = self.client.login(username='admin',password='admin')
        self.assertTrue(login_successful)

    def check_rendering(self,url,template):
        response = self.client.get('/profiles/edit/',follow=True)
        self.assertTrue(200, response.status_code)
        assert  response.context["user"].is_authenticated()
        self.assertTemplateUsed(response, 'profiles/edit.html')


    def test_profile(self):
        self.check_rendering('/profiles/edit/','profiles/edit.html')


    def test_game(self):
        self.check_rendering('/games/','games/index.html')   


    def test_game_wins(self):
        self.check_rendering('/games/wins/','games/wins.html')


    def test_game_losts(self):
        self.check_rendering('/games/losts/','games/losts.html')


    def test_game_draws(self):
        self.check_rendering('/games/draws/','games/draws.html')