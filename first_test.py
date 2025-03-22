import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wait = 5

# Variable declaration
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"
first_name = "Maxwell"
last_name = "Testing"
postal_code = "12345"

# Browser initialisation
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(wait)

#Login details
UserName = driver.find_element(By.ID, "user-name")
UserName.send_keys(username)

Password = driver.find_element(By.ID, "password")
Password.send_keys(password)

LoginButton = driver.find_element(By.ID, "login-button")
LoginButton.click()
time.sleep(wait)

#Add to cart
BackPack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
BackPack.click()
time.sleep(2)

BikeLight = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
BikeLight.click()
time.sleep(2)

BoltTshirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
BoltTshirt.click()
time.sleep(2)

FleeceJacket = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
FleeceJacket.click()
time.sleep(2)

Onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
Onesie.click()
time.sleep(2)

Tshirt_Red = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
Tshirt_Red.click()
time.sleep(3)

Cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
Cart.click()
time.sleep(wait)

# Go to cart & checkout details
Checkout = driver.find_element(By.ID, "checkout")
Checkout.click()
time.sleep(2)
FirstName = driver.find_element(By.ID, "first-name")
FirstName.send_keys(first_name)
LastName = driver.find_element(By.ID, "last-name")
LastName.send_keys(last_name)
PostalCode = driver.find_element(By.ID, "postal-code")
PostalCode.send_keys(postal_code)
time.sleep(2)
ContinueButton = driver.find_element(By.ID, "continue")
ContinueButton.click()
time.sleep(wait)

# Finish checkout process
Finish = driver.find_element(By.ID, "finish")
Finish.click()
time.sleep(wait)

BackToProducts = driver.find_element(By.ID, "back-to-products")
BackToProducts.click()
time.sleep(wait)

# Logout
Menu = driver.find_element(By.ID, "react-burger-menu-btn")
Menu.click()
time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(wait)