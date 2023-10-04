from bs4 import BeautifulSoup
import requests
import re


class PhoneParser:
    def __init__(self, url: str):
        self.html_page = None
        self.url = url

    def get_html(self):
        self.html_page = requests.get(self.url).text

    def search_numbers(self, tags=('a', 'div', 'p'), parser='lxml', clases=None) -> list:
        self.soup = BeautifulSoup(self.html_page, parser)
        all_numbers = []
        regex = r'(?:\+7|8)[ (]*\d{3}[ )]*\d{3}(?:[ -]\d{2}){2}'
        finded_tags = self.soup.find_all(tags)
        for i in finded_tags:
            number = re.findall(regex, i.text)
            if number:
                all_numbers.extend(number)
        return all_numbers

    def save_to_html(self, name):
        with open(name, mode='w', encoding='utf8') as f:
            f.write(self.html_page)


# example

pedant = PhoneParser('https://pedant.ru/')
pedant.get_html()  # сохраняем
print(pedant.search_numbers()) # выводим список номеров

