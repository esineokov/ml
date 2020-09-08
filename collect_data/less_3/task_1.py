# 1) Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
# записывающую собранные вакансии в созданную БД

import sys
from collect_data.less_2.task_1 import get_vacancy_from_sj, columns, get_vacancy_from_hh
from pymongo import MongoClient

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
    collection.remove()

    for m in (get_vacancy_from_sj, get_vacancy_from_hh):
        collection.insert_many(list(map(lambda x: dict(zip(columns, x)), m(keyword=keyword, n_pages=n_pages))))

