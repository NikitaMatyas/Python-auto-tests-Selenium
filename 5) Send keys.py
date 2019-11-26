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

# Ввод данных
element.send_keys('ZDAROVA')
time.sleep(3)
element.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').click()
time.sleep(3)

driver.quit()
