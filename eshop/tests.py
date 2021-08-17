from django.test import TestCase

# Create your tests here.
class Signup_Test(TestCase):

    def setUp(self):

        self.user = User.objects.create('pradip', None,'pradip','pradipchavanchaemail@gmail.com','1','male','student')
        self.user.save()

    def test_login_valid_user(self):
        user = authenticate(username='pradip',password = 'Pradip@7695')
        self.assertTrue((user is not None)and user.is_authenticated)

    def test_login_invalid_username(self):
        user = authenticate(username='wrong',password = 'Pradip@7695')
        self.assertFalse((user is not None)and user.is_authenticated)

    def test_login_invalid_pass(self):
        user = authenticate(username='wrong',password = 'Pradip7695')
        self.assertFalse((user is not None)and user.is_authenticated)


    def tearDown(self):
        self.user.delete()