from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get("https://google.com")

print(driver.current_url)
print(driver.title)
# print(driver.page_source)

driver.close()
