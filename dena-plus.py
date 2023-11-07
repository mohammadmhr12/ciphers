from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


def get_info(url, model, color):
    driver = webdriver.Edge()
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    end_of_scroll = driver.execute_script('return document.body.scrollHeight')

    cars_info = list()
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(5)
        my_scroll = driver.execute_script('return document.body.scrollHeight')
        if my_scroll == end_of_scroll:
            break
        end_of_scroll = my_scroll

        source_page = driver.page_source
        soup = BeautifulSoup(source_page, 'html.parser')
        cars = soup.find_all('div', {'class': 'post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46'})

        for car in cars:
            try:
                title = car.find('h2', {'class': 'kt-post-card__title'})
                mileage_price = car.find_all('div', {'class': 'kt-post-card__description'})
                mileage = int(mileage_price[0].text.strip('کیلومتر').replace(',', ''))
                price = int(mileage_price[1].text.strip('تومان').replace(',', ''))
                
                cars_info.append((title.text, mileage, price, model, color))
            except:
                pass
    
    cars_info = set(cars_info)
    return cars_info


def create_file():
    fields = ['title', 'mileage', 'price', 'model', 'color']
    with open('dena-plus.csv', 'a', encoding='utf8') as fin:
        write = csv.writer(fin)
        write.writerow(fields)


def add_data(cars_info):
    with open('dena-plus.csv', 'a', encoding='utf8') as fin:
        write = csv.writer(fin)
        write.writerows(cars_info)


if __name__ == "__main__":

    model = 1401

    urls = [
        "https://divar.ir/s/tehran/car/dena/plus?color=%D8%B3%D9%81%DB%8C%D8%AF&production-year=1401-1401",
        "https://divar.ir/s/tehran/car/dena/plus?color=%D9%86%D9%82%D8%B1%D9%87%E2%80%8C%D8%A7%DB%8C&production-year=1401-1401",
        "https://divar.ir/s/tehran/car/dena/plus?color=%D9%85%D8%B4%DA%A9%DB%8C&production-year=1401-1401",
        "https://divar.ir/s/tehran/car/dena/plus?color=%D8%AE%D8%A7%DA%A9%D8%B3%D8%AA%D8%B1%DB%8C&production-year=1401-1401",
    ]

    colors = [
        "white",
        "silver",
        "black",
        "gray",
    ]
    
    create_file()
    for url, color in zip(urls, colors):
        cars_info = get_info(url=url, model=model, color=color)
        add_data(cars_info=cars_info)
