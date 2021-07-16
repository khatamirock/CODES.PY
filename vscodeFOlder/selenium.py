from selenium import webdriver
from selenium.webdriver.chrome.options import Options

browserpath=r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
driverPath=r'D:\webDrive\chromedriver.exe'

options = Options()
options.binary_location = browserpath
driver = webdriver.Chrome(chrome_options=options, executable_path=driverPath )

driver.get('https://quranwbw.com/')









