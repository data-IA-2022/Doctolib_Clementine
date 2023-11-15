from django.test import TestCase
from django.contrib.auth import get_user_model

class UtilisateurModelTest(TestCase):

    def test_user_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='12345', role='patient')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.role, 'patient')
        self.assertTrue(user.check_password('12345'))

    def test_medecin_login(self):
        User = get_user_model()
        medecin = User.objects.create_user(username='medecintest', password='12345', role='medecin')
        login = self.client.login(username='medecintest', password='12345')
        self.assertTrue(login)