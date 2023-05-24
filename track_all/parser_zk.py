import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_info(address):
    data = []
    url = f"https://explorer.zksync.io/address/{address}"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Поиск всех элементов с классом "block-info-field-value"
    elements = soup.find_all('div', class_='block-info-field-value')

    # Извлечение значений из найденных элементов
    values = [element.text for element in elements]

    data.append(values[2])

    tables = soup.find_all('div', class_='table-container')
    second_table = tables[1]  # Индекс 1 соответствует второй таблице

    rows = second_table.find_all('tr')

    for row in rows:
        columns = row.find_all('td')

        if len(columns) >= 3:
            asset = columns[0].text.strip()
            balance = columns[1].text.strip()
            # token_address = columns[2].text.strip()

            # print(f"Asset: {asset}")
            data.append(asset)
            # print(f"Balance: {balance}")
            data.append(balance)
            # print(f"Token Address: {token_address}")
            # print("---")
    return data
