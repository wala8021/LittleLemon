from django.test import TestCase


class TestCall(TestCase):
    def test_register_new_user(self): #tests new user registration
        response = self.client.post("/auth/users/", data={"username":'user', "password":'test@2023'})
        self.assertEqual(response.status_code, 201)
        
