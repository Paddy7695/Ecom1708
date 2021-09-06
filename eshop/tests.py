'''from django.test import TestCase

# Create your tests here.
class Signup_Test(TestCase):

    def setUp(self):

        self.user = user.objects.create(Username='pradip',First_name='pradip',Last_name='chavan',password = 'Pradip@7695',Password_confirmation = 'Pradip@7695')
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
'''
l=[1,2]
print(id(l))
print(l)
l.append(3)
print(id(l))
print(l)

a=[10,25,5,3,1,40]
print(a)
print(id(a))
b=a
print(id(b))
print(b)
print(a)
print(id(a))
a.sort()
print(id(a))
print(a)
