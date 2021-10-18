from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from utils import delay

#  Initialize chrome driver
service = Service("/Users/benpinchas/Downloads/chromedriver")
driver = webdriver.Chrome(service=service)


def task_1():
   driver.get("https://www.walla.co.il")
# task_1()


def task_2():
   website_title  = driver.title
   driver.refresh()
   assert website_title == driver.title, "The titles are not identical"
# task_2()


# 4
def test_google_translate():
   driver.get("https://translate.google.com/?sl=iw&tl=en&op=translate")
   # Gave "hebrew_textarea" a type of "WebElement" in order to get code completion
   hebrew_textarea: WebElement = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea') 
   phrase = "שלום עולם"
   hebrew_textarea.send_keys(phrase)
   assert hebrew_textarea.get_attribute("value") == phrase, "Something wrong with google translate :o"
# test_google_translate()


@delay # delay - To see search results before moving on to the next website
def task_5():
   driver.get("https://youtube.com")
   searchbox_input: WebElement = driver.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
   searchbox_input.send_keys("2Pac - Changes")
   search_button: WebElement = driver.find_element(By.XPATH,'//*[@id="search-icon-legacy"]')
   search_button.click()
task_5()


@delay
def task_6():
   driver.get("https://translate.google.com/?sl=iw&tl=en&op=translate")
   # XPATH
   web_element_1: WebElement = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
   # CSS_SELECTOR
   web_element_2: WebElement = driver.find_element(By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd.nzsIKe > span > span > div > textarea')
   # CLASS_NAME
   web_element_3: WebElement = driver.find_element(By.CLASS_NAME, "er8xn")

   print(web_element_1, web_element_2, web_element_3)
task_6()


def task_7():
   driver.get("https://facebook.com")

   email_input: WebElement = driver.find_element(By.XPATH, '//*[@id="email"]')
   password_input: WebElement = driver.find_element(By.XPATH, '//*[@id="pass"]')
   submit_button: WebElement =  driver.find_element(By.XPATH,  '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

   email_input.send_keys("ben@gmail.com")
   password_input.send_keys("123456")
   submit_button.click()
task_7()


@delay
def task_8():
   driver.get("https://youtube.com")
   cookies = driver.get_cookies()
   print("Cookies in the browser:", cookies)
   driver.delete_all_cookies()
   cookies = driver.get_cookies()
   print("Cookies in the browser AFTER deletion:", cookies)
task_8()


@delay
def task_9():
   driver.get("https://github.com")
   searchbox_input: WebElement = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]')
   searchbox_input.send_keys("selenium")
   searchbox_input.send_keys(Keys.ENTER)
task_9()


def task_10():
   service = Service("/Users/benpinchas/Downloads/chromedriver")
   chrome_options = Options()
   chrome_options.add_argument("--disable-extensions")
   driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

   driver.get("http://facebook.com")
task_10()