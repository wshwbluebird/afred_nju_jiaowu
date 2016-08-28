#!/usr/local/Cellar/python/2.7.12/bin/python2.7
from selenium import webdriver


driver = webdriver.Chrome("/Users/wshwbluebird/tool/chromedriver")
base_url = "http://desktop.nju.edu.cn:8080/jiaowu"
driver.get(base_url + "/")
try:
    driver.find_element_by_name("userName").send_keys("xxxxxxx")
    driver.find_element_by_name("password").send_keys("xxxxxxx")
    driver.find_element_by_class_name("Btn").click()
except :
    print "failed"


