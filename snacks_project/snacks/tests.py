from django.test import SimpleTestCase
from django.urls import reverse

class SnacksTests(SimpleTestCase) :
    def test_home_page_status_code(self) :
        url = reverse('home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        
    def test_about_page_status_code(self) :
        url = reverse('about')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_home_page_template(self) :
        url = reverse('home')
        resp = self.client.get(url)
        self.assertTemplateUsed(resp, "home.html")
        self.assertTemplateUsed(resp, "_base.html")

    def test_about_page_template(self) :
        url = reverse('about')
        resp = self.client.get(url)
        self.assertTemplateUsed(resp, "about.html")
        self.assertTemplateUsed(resp, "_base.html")
