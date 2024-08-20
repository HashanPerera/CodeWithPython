# import the selenium-webdriver
from selenium import webdriver
# use By in find_element import class
from selenium.webdriver.common.by import By

# create a browser variable to call the Edge driver 
# In Python, an instance is a specific object created from a class, which is a blueprint for objects. When you create an instance of a class, you are essentially creating a unique copy of that class with its own set of attributes and methods.
browser = webdriver.Edge()

# call the maximise function
browser.maximize_window()

# call the browser URL
browser.get("http://www.automationpractice.pl/index.php")

# Locate to a variable the html element

# searchBarValue = browser.find_element(By.NAME, "search_query")
# searchBarValue.send_keys('Clothes')
# searchBarButton = browser.find_element(By.NAME, 'submit_search')
# searchBarButton.click()
SignIn = browser.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
SignIn.click()
TitleofPage = browser.title
print(f'\n Page title is "{TitleofPage}"')