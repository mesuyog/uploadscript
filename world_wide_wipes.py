# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class WorldWideWipes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.worldwidewives.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_world_wide_wipes(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("Teletabis")
        driver.find_element_by_name("pw").clear()
        driver.find_element_by_name("pw").send_keys("38ae3933")
        driver.find_element_by_name("login").click()
        driver.find_element_by_link_text("Upload").click()
        driver.find_element_by_css_selector("span.category").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("asa mindblowing blowjob")
        driver.find_element_by_name("msg").clear()
        driver.find_element_by_name("msg").send_keys("hello this is asa akira awesome video")
        #driver.find_element_by_name("file1").clear()
        driver.find_element_by_name("file1").send_keys("C:\\Users\\Sakuragi-Kun\\mystuff\\p240.mp4")
        driver.find_element_by_name("agreeterms").click()
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        for i in range(60):
            try:
                if "class=thanks-content" != driver.find_element_by_tag_name("BODY").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
