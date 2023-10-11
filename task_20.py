from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Task20:
   username = "standard_user"
   password = "standard_user"
   def __init__(self, web_url):
       self.url = web_url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


   def login(self):
       self.driver.maximize_window()
       self.driver.get(self.url)
       print(self.driver.title)
       print(self.driver.current_url)
       self.driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a').click()
       sleep(2)
       self.driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
       sleep(2)
       
      
        
def shutdown(self):
       self.driver.quit()




url = "https://www.cowin.gov.in/"


task = Task20(url)


task.login()


task.shutdown()

