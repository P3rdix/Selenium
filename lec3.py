from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime

# response to a new message in whatsapp

Group = ""
Message = "Hello, this is an automated message. Reply End to end program"

website = "https://web.whatsapp.com/"
options=Options()
options.add_argument('-profile')
options.add_argument('/home/vedant/Documents/Internship_Work/Internship2/Firefox/Web_Scraping')
driver = webdriver.Firefox(options=options,service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(400)
driver.get(website)

try: 
    searchbar = WebDriverWait(driver,40).until(EC.presence_of_element_located((By.XPATH,"//span[@title='"+Group+"']")))
except:
    driver.save_screenshot('ss.png')
    driver.quit()
    print("fail")

group = driver.find_element(By.XPATH, "//span[@title='"+Group+"']")
group.click()

prev = ""
print("Works till here")
inputs = driver.find_elements(By.XPATH,"//div[@class='message-in focusable-list-item _1AOLJ _2UtSC _1jHIY']//child::div/div/div/div/div/div/span[@class='_11JPr selectable-text copyable-text']")

for i in inputs:
    print(i.text)

while(True):
    inputs = driver.find_elements(By.XPATH,"//div[@class='message-in focusable-list-item _1AOLJ _2UtSC _1jHIY']//child::div/div/div/div/div/div/span[@class='_11JPr selectable-text copyable-text']")
    if prev!= inputs[-1].text:
        if inputs[-1].text == "End":
            break
        prev = inputs[-1].text
        txtbox = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
        time.sleep(1)
        txtbox.click()
        time.sleep(2)    
        for element in Message:
            txtbox.send_keys(element)
        time.sleep(1)
        btn = driver.find_element(By.CSS_SELECTOR, "Button[aria-label='Send']")
        btn.click()
    time.sleep(5)

driver.close()
driver.quit()