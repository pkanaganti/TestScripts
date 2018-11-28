import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

class admin_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver

        driver.get("http://pkanaganti.pythonanywhere.com/")
        time.sleep(1)

        elem = driver.find_element_by_xpath("//*[@id='app-layout']/nav/div/ul/li/a").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Logged In"
        time.sleep(2)
        data = open("service.csv")
        datareader = csv.reader(data)
        for row in datareader:
            if datareader.line_num == 1:
                continue
            else:
                cust_name = row[0]
                service_category= row[1]
                description = row[2]
                location = row[3]
                service_charge = row[4]
                # xpath, clicks on services button
                elem = driver.find_element_by_xpath("//*[@id='app-layout']/div[1]/a[3]").click()
                time.sleep(2)

                # xpath, clicks on add service button
                elem = driver.find_element_by_xpath("//*[@id='app-layout']/div[2]/div/div/div[2]/a/span").click()
                time.sleep(2)

                # fillig out the service form
                elem = driver.find_element_by_id("id_cust_name")
                elem.send_keys(cust_name)
                time.sleep(1)
                elem = driver.find_element_by_id("id_service_category")
                elem.send_keys(service_category)
                time.sleep(1)
                elem = driver.find_element_by_id("id_description")
                elem.send_keys(description)
                time.sleep(1)

                elem = driver.find_element_by_id("id_location")
                elem.send_keys(location)
                time.sleep(1)
                elem = driver.find_element_by_id("id_service_charge")
                elem.send_keys(service_charge)
                time.sleep(1)

                # xpath, clicks on save button
                elem = driver.find_element_by_xpath("//*[@id='app-layout']/div[2]/div/div/form/button").click()
                time.sleep(2)
        data.close()




    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()