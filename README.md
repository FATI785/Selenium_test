# ANST_Selenium_Test_Class
ANST_Selenium_Test_Class

Overview
This script automates the process of logging into the SauceDemo website,
adding multiple products to the cart, checking out, and logging out. It uses
Selenium WebDriver with Python to interact with the web elements.

Prerequisites
-Install Python 
-Install Google Chrome browser
-Install ChromeDriver (compatible with your Chrome version)
-Install Selenium using: pip install selenium

Script Functionality:
Opens the SauceDemo website.
Logs in with predefined credentials.
Adds six different items to the shopping cart.
Navigates to the cart and proceeds to checkout.
Fills in user details and completes the purchase.
Returns to the products page and logs out.

How to Run the Script:
Ensure all prerequisites are installed.
Save the script as first_test.py.

Notes
The script uses time.sleep() for wait times, which can be replaced with Selenium's implicit or explicit waits for better performance.
ChromeDriver should be updated to match the installed Chrome version.
Ensure a stable internet connection for smooth execution.

Author:
Fatimat Odukoya