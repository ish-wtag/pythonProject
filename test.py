import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("/Users/shikdershondhi/PycharmProjects/pythonProject/chromedriver")
#service_obj = Service("/Users/shikdershondhi/PycharmProjects/pythonProject/msedgedriver")
driver = webdriver.Chrome(service=service_obj, chrome_options =chrome_options)
#driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
#driver.minimize_window()
driver.get("https://wellautotng.staging.welltravel.com")
driver.save_screenshot('screenshot.png')
#driver.maximize_window()
#driver.close()
