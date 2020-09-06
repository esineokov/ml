# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы) с сайтов
# Superjob и HH. Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы).
# Получившийся список должен содержать в себе минимум:
# Наименование вакансии.
# Предлагаемую зарплату (отдельно минимальную и максимальную).
# Ссылку на саму вакансию.
# Сайт, откуда собрана вакансия.
# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
# Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью
# dataFrame через panda
import re
import sys
import urllib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

if len(sys.argv) < 2:
    exit("Incorrect incoming values\nPlease use:\n\tpython task_1.py vacancy_name [n]\nn - pages count (1 - default)")

timeout_s = 7
sj_host = "https://www.superjob.ru"
hh_host = "https://hh.ru"

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183."
              "83 Safari/537.36")

columns = ['Name', 'Salary min', 'Salary max', 'link', 'site']

keyword = sys.argv[1]
try:
    n_pages = int(sys.argv[2]) if len(sys.argv) == 3 else 1
except Exception as e:
    n_pages = 1

if n_pages == 0:
    n_pages = 1


def get_page(url):
    response = requests.get(url, timeout=timeout_s, headers={"user-agent": user_agent})
    return response.text


def text_to_salary(text):
    return "".join(re.findall("[0-9]+", text))


def get_vacancy_from_sj(keyword, n_pages=1):
    results = []
    for _ in range(n_pages):
        page = get_page(f"{sj_host}/vacancy/search/?keywords={keyword}&page={_}")
        soup = BeautifulSoup(page, features="html.parser")

        if 'Ничего не нашлось' in soup.text:
            break

        vacancies = [
            e for e in soup.find_all("div", attrs={'class': '_2g1F-'})
            if e.find("div", attrs={"class": "jNMYr GPKTZ _1tH7S"})
        ]
        for v in vacancies:
            name = v.find("a", attrs={"class": 'icMQ_'}).text
            salary = v.find("span", attrs={"class": '_1OuF_'}).text
            salary_min = salary_max = None
            if ' — ' in salary:
                min_, max_ = salary.split(" — ")
                salary_min, salary_max = text_to_salary(min_), text_to_salary(max_)
            elif 'до ' in salary:
                salary_max = text_to_salary(salary)
            elif 'от ' in salary:
                salary_min = text_to_salary(salary)
            else:
                salary_min = salary_max = salary

            link = urllib.parse.urljoin(sj_host, v.find("a", attrs={"class": 'icMQ_'}).attrs['href'])
            site = sj_host
            results.append((name, salary_min, salary_max, link, site))
    return results


def get_vacancy_from_hh(keyword, n_pages=1):
    results = []
    for _ in range(n_pages):
        page = get_page(f"{hh_host}/search/vacancy?text={keyword}&page={_}")
        soup = BeautifulSoup(page, features="html.parser")

        if 'Ошибка 404' in soup.text:
            break

        vacancies = soup.find_all("div", attrs={'class': 'vacancy-serp-item__row vacancy-serp-item__row_header'})
        for v in vacancies:
            name = v.find("span", attrs={"class": 'resume-search-item__name'}).text
            salary = v.find("div", attrs={"class": 'vacancy-serp-item__sidebar'}).text
            salary_min = salary_max = None
            if '-' in salary:
                min_, max_ = salary.split("-")
                salary_min, salary_max = text_to_salary(min_), text_to_salary(max_)
            elif 'до ' in salary:
                salary_max = text_to_salary(salary)
            elif 'от ' in salary:
                salary_min = text_to_salary(salary)
            else:
                salary_min = salary_max = salary

            link = v.find("a", attrs={"data-qa": 'vacancy-serp__vacancy-title'}).attrs['href'].split("?")[0]
            site = hh_host
            results.append((name, salary_min, salary_max, link, site))
    return results


df_sj = pd.DataFrame(get_vacancy_from_sj(keyword=keyword, n_pages=n_pages), columns=columns)
df_hh = pd.DataFrame(get_vacancy_from_hh(keyword=keyword, n_pages=n_pages), columns=columns)
print(tabulate(df_sj.append(df_hh), headers='keys', tablefmt='psql'))

