from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Importing and running selenium

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://selenium.dev")
print(driver.title)

driver.quit()

