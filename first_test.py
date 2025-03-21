import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(3)

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(4)

driver.find_element(By.ID, "checkout").click()
time.sleep(2)
driver.find_element(By.ID, "first-name").send_keys("Maxwell")
driver.find_element(By.ID, "last-name").send_keys("Testing")
driver.find_element(By.ID, "postal-code").send_keys("12350")
time.sleep(2)
driver.find_element(By.ID, "continue").click()
time.sleep(3)

driver.find_element(By.ID, "finish").click()
time.sleep(3)

driver.find_element(By.ID, "back-to-products").click()
time.sleep(4)

driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(5)

