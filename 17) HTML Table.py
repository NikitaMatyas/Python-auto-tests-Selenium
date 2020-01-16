from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('http://testautomationpractice.blogspot.com/')
driver.implicitly_wait(10)

# find_elements используется чтобы найти все строки в таблице, селектор без указания номера конкретной строки
rows_selector = driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr')
rows_number = len(rows_selector)

columns_selector = driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th')
columns_number = len(columns_selector)

print('Number of rows =', rows_number, '\nNumber of columns =', columns_number)

for row in range(2, rows_number + 1):
    for column in range(1, columns_number + 1):
        value = driver.find_element_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr['+str(row)+']/td['+str(column)+']').text
        print(value, end='  ')
    print()

driver.quit()
