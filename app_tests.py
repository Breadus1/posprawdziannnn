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

    def test_delete_user(self):
        response = self.test_client.delete('/users/2')  
        self.assertIn(response.status_code, [204, 404])

if __name__ == '__main__':
    unittest.main()
