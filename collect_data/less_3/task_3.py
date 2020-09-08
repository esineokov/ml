# 3) Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта

import sys
import pymongo.errors
from collect_data.less_2.task_1 import get_vacancy_from_sj, columns, get_vacancy_from_hh
from pymongo import MongoClient


def insert(m_collection, data):
    try:
        m_collection.insert(doc_or_docs=data, continue_on_error=True)
    except pymongo.errors.DuplicateKeyError:
        pass


if __name__ == "__main__":

    if len(sys.argv) < 2:
        exit(
            "Incorrect incoming values\nPlease use:\n\tpython task_1.py vacancy_name [n]\nn - pages count (1 - default)"
        )

    keyword = sys.argv[1]
    try:
        n_pages = int(sys.argv[2]) if len(sys.argv) == 3 else 1
    except Exception as e:
        n_pages = 1

    if n_pages == 0:
        n_pages = 1

    client = MongoClient()
    db = client['less_3']
    collection = db['vacancy']

    collection.create_index([('link', 1)], unique=True)

    for m in (get_vacancy_from_sj, get_vacancy_from_hh):
        insert(collection, list(map(lambda x: dict(zip(columns, x)), m(keyword=keyword, n_pages=n_pages))))
