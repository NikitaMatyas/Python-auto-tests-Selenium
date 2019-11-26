from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.maximize_window()

driver.get("https://google.com")

# Получить тайтл страницы
print(driver.current_url)
print(driver.title)
print(driver.page_source)

# driver.close()  # Close the browser window that the driver has focus of
driver.quit()  # Closes all browser windows and safely ends the session / destroy the web driver instance
