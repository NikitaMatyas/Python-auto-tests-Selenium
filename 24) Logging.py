from selenium import webdriver
import time
import logging

#chrome_path = r'C:\Users\anduser\Drivers\chromedriver_win32\chromedriver.exe'
#driver = webdriver.Chrome(executable_path=chrome_path)

#driver.get('http://amazon.com')
#driver.implicitly_wait(10)

logging.basicConfig(filename=r'C:\Users\anduser\Logs for Selenium\test.log',
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d/%m/%Y %H:%M:%S', level=logging.DEBUG)

'''
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
'''

# Через объект
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug('Debug message')

#time.sleep(3)
#driver.quit()
