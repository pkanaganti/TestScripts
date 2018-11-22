import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class admin_login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver

       driver.get("http://pkanaganti.pythonanywhere.com/")
       time.sleep(3)

       elem = driver.find_element_by_xpath("//*[@id='app-layout']/nav/div/ul/li/a").click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(2)
       assert "Logged In"
       time.sleep(2)
       # find element by xpath, click on service
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/p[2]/a").click()
       time.sleep(2)
       # find element by xpath, click on add service
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/div[2]/div/div/div[2]/a/span").click()
       time.sleep(3)

       elem = driver.find_element_by_id("id_cust_name")
       elem.send_keys("Bill Davis")
       time.sleep(2)
       elem = driver.find_element_by_id("id_service_category")
       elem.send_keys(" Food Delivery")
       time.sleep(2)
       elem = driver.find_element_by_id("id_description")
       elem.send_keys("Lunch-for 40 people")
       time.sleep(2)
       elem = driver.find_element_by_id("id_location")
       elem.send_keys("CPACS-120")
       time.sleep(2)

       elem = driver.find_element_by_id("id_service_charge")
       elem.send_keys("450")
       time.sleep(2)
        #xpath to save
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/div[2]/div/div/form/button").click()
       time.sleep(5)
      

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

