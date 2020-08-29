import requests
import json
from bs4 import BeautifulSoup as bs


HEADERS = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

def stop_covid_parser():

    
    url = "https://xn--80aesfpebagmfblc0a.xn--p1ai/#"

    session = requests.Session() # создание сессии запроса

    request = session.get(url, headers=HEADERS) # получение страницы

    #print(request)

    if request.status_code == 200:
    
        soup = bs(request.content, "html.parser")

        trs = soup.find_all("tr")

        trs = trs[0:81]

        #print(trs)

        cities_name = []

        cities_cases = []

        for tr in trs:

            cities_name.append(tr.find("th").text)

            tds = tr.find_all("td")

            #print(tds)

            one_city_cases = []

            one_city_cases.append(tds[0].text) # sick

            one_city_cases.append(tds[1].text) # recov

            one_city_cases.append(tds[2].text) # dead

            cities_cases.append(one_city_cases)

        
        cities_and_cases = dict(zip(cities_name, cities_cases))

        #print(cities_and_cases)

        with open("from_stop_covid.json", "r+", encoding="utf-8") as file: # запись в файл
                file.seek(0)
                file.write(json.dumps(cities_and_cases, ensure_ascii=False, indent=4))
                file.truncate()            

    else:
        print("error")

stop_covid_parser()