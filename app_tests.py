import unittest
import main

class UserManagementTests(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.test_client = main.app.test_client()

    def test_list_users(self):
        response = self.test_client.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        new_user = {'firstName': 'Marcel', 'lastName': 'Wątruch', 'birthYear': 1990, 'group': 'user'}
        response = self.test_client.post('/users', json=new_user)
        self.assertEqual(response.status_code, 201)

    def test_update_user(self):
        user_update = {'firstName': 'Jane'}
        response = self.test_client.patch('/users/2', json=user_update)  
        self.assertIn(response.status_code, [200, 404])

    def test_delete_user(self):
        response = self.test_client.delete('/users/2')  
        self.assertIn(response.status_code, [204, 404])

    def test_view_user(self):
        response = self.test_client.get('/users/2')  
        self.assertIn(response.status_code, [200, 404])



if __name__ == '__main__':
    unittest.main()
