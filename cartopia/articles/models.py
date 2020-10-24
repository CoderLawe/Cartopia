from django.db import models
from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.caranddriver.com/reviews/").text
soup = BeautifulSoup(source, 'lxml')


# Create your models here.
class Article(models.Model):
    manufacturer = models.CharField(max_length=200)
    carmodel = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.manufacturer

    def snippet(self):
        return self.body[:50] + '...'


def tickle(request):
    for article in soup.find_all('div', class_='full-item'):
        headline = article.find('a', class_='full-item-title item-title').text
