from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_model(self):
        c = Client()
        response = c.get('/main/')
        context_test = {
        'nama': 'Matthew Hotmaaja Johan Turnip',
        'npm' : '2206081231',
        'kelas': 'PBP C'
        }
        self.assertEqual(response.context['nama'], 'Matthew Hotmaraja Johan Turnip')
        self.assertEqual(response.context['npm'], '2206081231')
        self.assertEqual(response.context['kelas'], 'PBP C')