# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import random
import configparser

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
username=config['chihlee']['username']
password=config['chihlee']['password']

class TestSISystem1():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sISystem1(self):
    self.driver.get("http://140.131.77.93/SISystem/stdLogin.aspx")
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.ID, "U").click()
    self.driver.find_element(By.ID, "U").send_keys(username)
    self.driver.find_element(By.CSS_SELECTOR, ".contLeftCell").click()
    self.driver.find_element(By.ID, "P").click()
    self.driver.find_element(By.ID, "P").send_keys(password)
    self.driver.find_element(By.ID, "btnLogin").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td > .fntContBlock a").click()
    self.driver.find_element(By.LINK_TEXT, "◎ 期末教學評量").click()
    setPING=self.driver.find_element(By.XPATH, "(//a[contains(text(),\'開始評量\')])[1]")
    while(setPING):
      setPING.click()
      soup=BeautifulSoup(self.driver.page_source,"lxml")
      PINGtext=str(soup.find("div",style="font-size:17px; font-weight:bold;").text).strip()
      if(PINGtext!="導師評量"):
        radio=0
        while True:
          try:
            if(radio!=1):
              self.driver.find_element(By.ID, f"Radio1_{str(radio)}").click()
            else:
              self.driver.find_element(By.ID, f"Radio5_{str(radio)}").click()
          except:
            break
          radio+=1
        self.driver.find_element(By.ID, "Button1").click()
        self.driver.switch_to.alert.accept()
        setPING=self.driver.find_element(By.XPATH, "(//a[contains(text(),\'開始評量\')])[1]")
      else:
          for radio in range(0,27):
            if(radio!=21 and radio!=22 and radio!=23):
              self.driver.find_element(By.ID, f"Radio1_{str(radio)}").click()
            else:
              print(radio)
              self.driver.find_element(By.ID, f"Radio5_{str(radio)}").click()
          self.driver.find_element(By.ID, "Button1").click()
          self.driver.switch_to.alert.accept()
          break
chihlee=TestSISystem1()
chihlee.setup_method()
chihlee.test_sISystem1()
