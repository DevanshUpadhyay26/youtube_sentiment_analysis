from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

# Specify the path to ChromeDriver
chrome_service = Service(r'C:/chromedriver.exe')

# Initialize ChromeDriver with the Service object
with Chrome(service=chrome_service) as driver:
    driver.get("https://www.google.com")
    print("ChromeDriver is working!")
