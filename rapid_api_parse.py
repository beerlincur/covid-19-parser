import json # модуль для работы с json

import requests # модуль для получения страницы

from config import HEADERS # заголовки браузера для корректной работы


def rapid_api_parser():

    try:

        url = "https://covid19-server.chrismichael.now.sh/api/v1/allReports" # URL Api

        session = requests.Session() # создание сессии для обращения к url

        request = session.get(url, headers=HEADERS) # получение страницы
        if request.status_code == 200: # если страница получена:

            with open("from_rapid_api.json", "r+", encoding="utf-8") as file: # запись в файл
                file.seek(0)
                file.write(json.dumps(request.json(), ensure_ascii=False, indent=4))
                file.truncate()

        else:
            print(f"error with parsing api. Request code: {request.status_code}.")
    
    except Exception:

        print(Exception.message)
