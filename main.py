from rapid_api_parse import rapid_api_parser
from yandex_parse import yandex_parser
import time

def main():
    
    while(True):
        
        try:
            print("parsing yandex...")
            yandex_parser() # вызов парсера яндекса
            print("done.")

            print("parsing api...")
            rapid_api_parser() # вызов парсера апи
            print("done.")

            print("waiting for 5 minuts...")
            time.sleep(300) # передышка
            print("done.")

        except Exception: # обработка ошибок
            print(Exception.message)


if __name__ == "__main__":
    main()