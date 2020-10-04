# 2) Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введенной суммы.
# Поиск по двум полям (мин и макс зарплату)
import sys
import pandas as pd
from pymongo import MongoClient
from tabulate import tabulate

from collect_data.less_2.task_1 import columns

if __name__ == "__main__":

    if len(sys.argv) < 1:
        exit(
            "Incorrect incoming values\nPlease use:\n\tpython task_2.py salary_int"
        )

    try:
        salary = int(sys.argv[1]) if len(sys.argv) == 2 else 0
    except Exception as e: 
        salary = 0

    client = MongoClient()
    db = client['less_3']
    collection = db['vacancy']
    result = collection.find({'$or': [{'Salary min': {'$gt': salary}}, {'Salary max': {'$gt': salary}}]})

    df = pd.DataFrame(result, columns=columns)
    print(tabulate(df, headers='keys', tablefmt='psql'))
