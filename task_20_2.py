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
       self.driver.find_element(by=By.XPATH, value='/html/body/nav/div/div/div/ul/li[7]/a').click()
       sleep(2)
       self.driver.find_element(by=By.XPATH, value='/html/body/nav/div/div/div/ul/li[7]/ul/li[1]/a').click()
       sleep(2)
       self.driver.find_element(by=By.XPATH, value='//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').click()
       sleep(2)
       
      
        
def shutdown(self):
       self.driver.quit()




url = "https://labour.gov.in/"


task = Task20(url)


task.login()

