
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

def before_scenario(context,scenario):
    chrome_options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    context.wait = WebDriverWait(context.driver, 10)

def after_scenario(context,scenario):
    if hasattr(context, "driver"):
        context.driver.close()