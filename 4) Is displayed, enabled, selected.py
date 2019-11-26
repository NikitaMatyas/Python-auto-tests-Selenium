from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Указание пути к драйверу и сохранение
chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.maximize_window()

# Открыть страницу по URL
driver.get("https://google.com")
element = driver.find_element_by_name('q')

# Проверка отображения элемента
print(element.is_displayed())

# Проверка доступности элемента
print(element.is_enabled())

# Проверка выбран элемент или нет (напр. радио баттон)
print(element.is_selected())