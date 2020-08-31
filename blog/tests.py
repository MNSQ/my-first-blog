from django.test import TestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome()
browser = webdriver.Chrome()
browser.get('http://127.0.0.1:8000/')

assert 'Django' in browser.title
# Create your tests here.
