from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Automated messaging to Whatsapp using group and message


def send_message(msg, t="s", group="testing"):    
    website = "https://web.whatsapp.com/"
    options=Options()
    options.add_argument('-profile')
    options.add_argument('/home/vedant/Documents/Internship_Work/Internship2/Firefox/Web_Scraping')
    driver = webdriver.Firefox(options=options,service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(400)
    driver.get(website)
    try: 
            searchbar = WebDriverWait(driver,40).until(EC.presence_of_element_located((By.XPATH,"//span[@title='"+group+"']")))
    except:
        driver.save_screenshot('ss.png')
        driver.quit()
        print("fail")

    group = driver.find_element(By.XPATH, "//span[@title='"+group+"']")
    group.click()

    txtbox = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    time.sleep(4)
    txtbox.click()

    if t=="s":
        time.sleep(4)    
        for element in msg:
            txtbox.send_keys(element)
        time.sleep(4)
        btn = driver.find_element(By.CSS_SELECTOR, "Button[aria-label='Send']")
        btn.click()
    else:
        for item in msg:
            txtbox.click()
            time.sleep(2)
            for element in item:
                txtbox.send_keys(element)
            time.sleep(2)
            btn = driver.find_element(By.CSS_SELECTOR, "Button[aria-label='Send']")
            btn.click()
    time.sleep(15)
    driver.close()
    driver.quit()

# def send_message(msg, t="s", group="testing"):    
#     website = "https://web.whatsapp.com/"
#     options=Options()
#     options.add_argument('-profile')
#     options.add_argument('/home/vedant/Documents/Internship_Work/Internship2/Firefox/Web_Scraping')
#     driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
#     driver.implicitly_wait(400)
#     driver.get(website)
#     try: 
#         group = WebDriverWait(driver,40).until(EC.presence_of_element_located((By.XPATH,"//span[@title='Nachiket']")))
#         group.click()
#     except:
#         driver.save_screenshot('ss.png')
#         driver.quit()
#         print("fail")
#     print("C2")
#     txtbox = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
#     txtbox.click()
#     btn = driver.find_element(By.CSS_SELECTOR, "Button[aria-label='Send']")
#     btn.click()
#     time.sleep(10)
#     driver.close()
#     driver.quit()

send_message("Hello", group="Nachiket")