import os
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

os.environ['PATH'] += r"C:\Users\Alex\Desktop\Apps\web_scraping_selenium\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.pexels.com/photo/pink-flowers-photograph-1083822/")
# wait 3 seconds for page load ( does not wait for 3 seconds but starts as soon as element is found )
driver.implicitly_wait(3)
download_button = driver.find_element_by_xpath("//*[@id='photo-page-top']/div/div[2]/div/div/div/div/a")
download_button.click()


link = r"C:\Users\Alex\Downloads\pexels-lisa-1083822.jpg"
my_file = Path(link)
while not my_file.is_file():
  print("Not there yet")
  print("Sleep")
  time.sleep(1)
  my_file = Path(link)

print("File Downloaded!")
driver.close()
