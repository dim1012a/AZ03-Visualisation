from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

url = 'https://guitarlavka.ru/'

# Инициализируем веб-драйвер
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get(url)
    # Подождем, чтобы страница загрузилась
    time.sleep(90)  # Можно использовать более продвинутые методы ожидания
    # Получаем все элементы с ценами
    price_elements = driver.find_elements(By.CLASS_NAME, 'pop-pr-l-txt-2.pricecontainer')
    # Извлекаем текст цен и очищаем его
    prices = []
    for element in price_elements:
        price_text = element.text
        # Убираем пробелы и другие символы, оставляя только цифры и запятую
        price = ''.join(filter(lambda x: x.isdigit() or x == ',', price_text))
        prices.append(price)

    # Записываем цены в файл CSV
    with open('guitars.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])
        for price in prices:
            writer.writerow([price])

finally:
    # Закрываем драйвер
    driver.quit()
print("Цены успешно сохранены в файл guitars.csv")