from selenium import webdriver
import time
import pprint

chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('http://amazon.com')
driver.implicitly_wait(10)

# Capture all cookies from the browser
cookies = driver.get_cookies()

# Count number of cookies
print(len(cookies))

# Read cookie parts
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(cookies)

# Adding new cookies
cookie = {'name': 'MyCookie', 'value': '123456'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))
pp.pprint(cookies)

# Deleting specific cookie by using name of cookie
driver.delete_cookie('MyCookie')
cookies = driver.get_cookies()
print(len(cookies))
pp.pprint(cookies)

# Deleting all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))

time.sleep(3)
driver.quit()
