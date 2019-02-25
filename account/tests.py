from django.test import TestCase
from account import models as amod
from django.contrib.auth import models as pmod
from lxml import etree
from datetime import datetime
import random
# Create your tests here.

class AccountTests(TestCase):
    fixtures = ['account.yaml']

#have to name it with test if you want it to be a unit test
    def test_user_get(self):
        u1 = amod.User.objects.get(id=2)
        self.assertEqual(u1.first_name, 'Red', msg="Name should have been Red")

    def test_user_create(self):
        u = amod.User()
        u.first_name = 'TWICE'
        u.last_name = 'Twice'
        u.email = "twice@jyp.com"
        u.username = "twicetwice"
        u.set_password("yesoryes")
        u.save()
        u2 = amod.User.objects.get(username=u.username)

        self.assertEqual(u.first_name, u2.first_name, msg="...")

    def setUp(self):
        # I'm creating a user here (instead of use one from the fixtures)
        # because you students probably don't have the same users in fixtures.
        self.homer = amod.User()
        self.homer.username = "homer2"
        self.homer.set_password('doh!')
        self.homer.first_name = "Homer"
        self.homer.last_name = "Simpson"
        self.homer.birthdate = datetime(2000, 1, 1)
        self.homer.save()

    def test_user_login(self):
        credentials = {
            'username': 'homer2',
            'password': 'doh!'
        }
        response = self.client.post('/account/login/', credentials)
        # get the request object (testing framework embeds it as response.wsgi_request)
        request = response.wsgi_request
        # this next line is ONLY for debugging the test - it should be removed after things work
        self.print_html(response.content)
        # if it worked, then request.user will be the homer object and is_authenticated will be true
        self.assertTrue(request.user.is_authenticated, msg="User should have authenticated")
        self.assertEqual(request.user.id, self.homer.pk, msg="User should have been homer")
        # if it worked, the response should be a redirect code (login.py returned HttpResponseRedirect)
        self.assertEqual(response.status_code, 302, msg="User wasn't redirected")

    def test_user_logout(self):
        response = self.client.post('/account/logout/')
        request = response.wsgi_request
        self.assertFalse(request.user.is_authenticated, msg="User should not have authenticated")

    def test_reset_password (self):
        u = amod.User.objects.get(pk = 2)
        x = random.randint(1,1001)
        u.set_password('new password' + str(x))
        u.save()
        self.assertTrue(u.check_password('new password' + str(x)), msg="Unable to reset password")

    def test_user_permissions(self):
        p = pmod.Permission()
        p.codename = 'winmyheart'
        p.name = 'Win Over my heart'
        p.content_type = pmod.Permission.objects.get(codename='add_user').content_type
        p.save()

        ispermissionsaved = False

        for p in pmod.Permission.objects.all():
             if p.codename == 'winmyheart':
                 ispermissionsaved = True

        self.assertTrue(ispermissionsaved, msg="Permission was not created")

        u = amod.User.objects.get(username='redvelvet')
        u.user_permissions.add(pmod.Permission.objects.get(codename='winmyheart'))

        self.assertEqual(u.get_all_permissions(),{'account.winmyheart'}, msg="User did not get permission")

    def test_group_permissions(self):
        g1 = pmod.Group()
        g1.name = 'TestGroup'
        g1.save()

        g1 = pmod.Group.objects.get(name='TestGroup')

        self.assertEqual(g1.name, 'TestGroup', msg='Didnt save group')

        g1.permissions.add(pmod.Permission.objects.get(codename='add_user'))
        g1.permissions.add(pmod.Permission.objects.get(codename='delete_user'))

        u = amod.User.objects.get(pk=self.homer.pk)
        u.groups.add(pmod.Group.objects.get(name='TestGroup'))

               
        self.assertEqual(u.get_all_permissions(), {'account.add_user', 'account.delete_user'}, msg="Group was not added to homer")

    def print_html(self, content):
        '''Helper to pretty-print HTML'''
        content = content.strip()
        if content:
            html = etree.HTML(content)
            print(etree.tostring(html, pretty_print=True, encoding=str))
        else:
            print('<empty content>')