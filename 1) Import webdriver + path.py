from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Указание пути к драйверу и сохранение
chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.maximize_window()

# Открыть страницу по URL
driver.get("https://google.com")