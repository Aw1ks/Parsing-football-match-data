import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import pandas as pd
from terminaltables import SingleTable


custom_optioms = Options()
custom_optioms.add_argument("--start-maximized")
driver = webdriver.Chrome(options=custom_optioms)
link = 'https://www.flashscore.com.ua/.'
driver.get(link)
time.sleep(60)


driver_m = driver.find_elements(By.CLASS_NAME, 'event__match.event__match--twoLine')
dict_drivers = []

table = [
    ['stat', 't1', 't2', 'g1', 'g2']
]

for driver in driver_m:
    formatted_driver = driver.text.splitlines()

    table.append([
        formatted_driver[0],
        formatted_driver[1],
        formatted_driver[2],
        formatted_driver[3],
        formatted_driver[4],
    ])


df = pd.DataFrame(table[1:], columns=table[0])

completed_matches = df[df['stat'].str.contains('Завершен', na=False)]
print(completed_matches)

df.to_excel('Парсинг данных футбольных матчей.xlsx', index=False, engine='openpyxl')
