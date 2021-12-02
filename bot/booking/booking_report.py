from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BookingReport:
  def __init__(self, boxes: WebElement, driver):
    self.driver = driver
    self.boxes = boxes
    
  def get_report(self):
    collection = []
    for box in self.boxes:
      title = box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute('innerHTML').strip()
      price = box.find_element(By.CSS_SELECTOR, 'div[data-testid="price-and-discounted-price"]').find_element(By.TAG_NAME, 'span').get_attribute('innerHTML').strip().replace('&nbsp;', '')
      hotel_score = ''
      self.driver.implicitly_wait(0)
      try:
        hotel_score = box.find_element(By.CSS_SELECTOR, 'div[data-testid="review-score"]').find_element(By.TAG_NAME, 'div').get_attribute('innerHTML').strip()
      except:
        hotel_score = "Externally rated"
      collection.append([title, price, hotel_score])
    return collection