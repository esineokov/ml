# Написать приложение, которое собирает основные новости с сайтов news.mail.ru, lenta.ru, yandex-новости.
# Для парсинга использовать XPath. Структура данных должна содержать:
# название источника;
# наименование новости;
# ссылку на новость;
# дата публикации.
import re
from lxml import html
from datetime import datetime
import xml.etree.ElementTree as ET
import requests
from tabulate import tabulate

timeout_s = 7
user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183."
              "83 Safari/537.36") 


class Parser:
    def get_page(self, url):
        response = requests.get(url, timeout=timeout_s, headers={"user-agent": user_agent})
        return response.text


class Mail(Parser):
    def __init__(self):
        self.host = "https://news.mail.ru/rss/90/"

    def get_news(self):
        result = []
        news = ET.fromstring(self.get_page(self.host))
        for new in news.findall("*//item"):
            link = new.find("link").text
            title = new.find("title").text
            pub_date = datetime.strptime(new.find("pubDate").text, '%a, %d %b %Y %X %z')
            result.append(("news.mail.ru", link, title, pub_date))
        return result


class Yandex(Parser):
    def __init__(self):
        self.host = "https://yandex.ru/news"

    def get_news(self):
        result = []
        news = html.fromstring(self.get_page(self.host))
        for new in news.xpath("//article[contains(@class, 'news-card')]"):
            link = new.xpath(".//a[@class='news-card__link']/@href")[0]
            title = new.xpath(".//a[@class='news-card__link']/h2[@class='news-card__title']/text()")[0]
            pub_date = new.xpath(".//span[@class='mg-card-source__time']/text()")[0]
            if re.match("[0-9]{2}:[0-9]{2}", pub_date):
                pub_date = datetime.today().strptime(f"{datetime.today().strftime('%Y %m %d')} {pub_date}",
                                                     '%Y %m %d %H:%M')
            result.append(("yandex.ru", link, title, pub_date))
        return result


class Lenta(Parser):
    def __init__(self):
        self.host = "https://lenta.ru"

    def get_news(self):
        result = []
        lenta_news = html.fromstring(self.get_page(self.host))
        for new in lenta_news.xpath(
                ("//a[starts-with(@href, '/news/') and not(contains(@class, 'topic-title-pic__link')) and ./time and ./"
                 "text()]")
        ):
            link = f"{self.host}{new.xpath('@href')[0]}"
            title = new.xpath("./text()")[0]
            pub_date = new.xpath('./time/@datetime')
            if pub_date:
                pub_date = pub_date[0]
            result.append(("lenta.ru", link, title, pub_date))

        for new in lenta_news.xpath("//div[contains(@class, 'item') and contains(@class, 'article')]"):
            try:
                link = f"{self.host}{new.xpath('*//a[./span]/@href')[0]}"
                title = new.xpath('*//a/span/text()')[0]
                pub_time = new.xpath('*//span[contains(@class, "g-date")]/span/text()')[0]
                pub_date = new.xpath('*//span[contains(@class, "g-date")]/text()')[0]
                result.append(("lenta.ru", link, title, f"{pub_date} {pub_time}"))
            except:
                pass
        return result


news = []
for i in (Yandex(), Mail(), Lenta()):
    news.extend(i.get_news())

print(tabulate(news, headers='keys', tablefmt='psql'))

