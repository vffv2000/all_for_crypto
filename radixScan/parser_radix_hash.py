import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_info(hash):
    info = []

    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = f'https://www.radixscan.io/search/{hash}'
    driver.get(url)
    time.sleep(5)

    table = driver.find_element(By.ID, 'datatable1')
    rows = table.find_elements(By.TAG_NAME, 'tr')

    for row in rows:

        cells = row.find_elements(By.TAG_NAME, 'td')
        for cell in cells:
            try:
                link_element = cell.find_element(By.TAG_NAME, 'a')
                link = link_element.get_attribute('href')
                if 'address' in link:
                    info.append(link[33:])
                elif "token" in link:
                    info.append(link[31:])
            except:
                values = cell.text
                info.append(values)
    element = driver.find_element(By.ID, 'Message')
    text = element.text
    info.append(text)
    # print(info)
    return info


