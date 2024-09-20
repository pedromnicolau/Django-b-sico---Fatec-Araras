from django.test import TestCase

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/natal')

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_texto(self):
        self.assertContains(self.resp, 'natal')

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'natal.html')

class AnoNovoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/ano_novo')

    def test_200_response(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_texto(self):
        self.assertContains(self.resp, 'ano novo')

    
