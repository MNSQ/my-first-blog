from django.urls import resolve
from django.test import TestCase
from lists.views import home_page  
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)  

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = self.client.get('/')
        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')s
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>MNSQ BLOG</title>', html)  
        self.assertTrue(html.strip().endswith('</html>'))
        ​self.assertTemplateUsed(response, 'wrong.html') 

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

# Create your tests here.
