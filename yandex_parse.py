import json # модуль для работы с json

import requests # модуль для получения страницы

from bs4 import BeautifulSoup as bs # модуль для парсинга страницы
from config import HEADERS # заголовки браузера
from lxml import html # для парсинга html


def yandex_parser():

    base_url = "https://yandex.ru/maps/covid19?ll=46.737291%2C-3.537040&z=2" # url

    session = requests.Session() # создание сессии запроса

    request = session.get(base_url, headers=HEADERS) # получение страницы

    if request.status_code == 200: # если страница получена:

        soup = bs(request.content, "html.parser") # преобразование в html

        cities_divs = soup.find_all("td", attrs={'class': "covid-table-view__item-name"}) # поиск городов

        cases_divs = soup.find_all("td", attrs={'class': "covid-table-view__item-cases"}) # поиск чисел по городам

        cities_and_cases_dict_divs = dict(zip(cities_divs, cases_divs)) # словарь для найденных тегов

        cases = [] # массив для конечных чисел

        cities = [] # массив для конечных названий

        for city, case in cities_and_cases_dict_divs.items(): # заполнение конечных массивов
            cases.append(case.text)
            cities.append(city.text)
        
        cities_and_cases_dict = dict(zip(cities, cases)) # формирование словаря для json

        values_divs = soup.find_all('div', attrs={'class': "covid-stat-view__item-value"}) # поиск статистических данных

        titles_divs = soup.find_all('div', attrs={'class': "covid-stat-view__item-title"}) # поиск заголовков

        bar_divs = dict(zip(titles_divs, values_divs)) # формирование словаря для найденных тегов

        values = [] # массив значений

        titles = [] # массив заголовков
        
        for title, value in bar_divs.items(): # заполнение массивов
            values.append(value.text)
            titles.append(title.text)

        bar_dict = dict(zip(titles, values)) # словарь для json 

        main_dict = {"bar" : bar_dict, "cities": cities_and_cases_dict} # главный словарь для записи в файл

        with open("from_yandex.json", "r+", encoding="utf-8") as file: # запись в файл
            file.seek(0)
            file.write(json.dumps(main_dict, ensure_ascii=False, indent=4))
            file.truncate()

    else:
        print(f"error with parsing yandex. Request code: {request.status_code}.")

    

print(yandex_parser())