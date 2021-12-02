from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BookingFiltration():
  def __init__(self, driver: WebDriver):
    self.driver = driver
    
  def apply_star_rating(self, *desired_rating):
    star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
    star_child_elements = star_filtration_box.find_elements(By.TAG_NAME, 'input')
    for input in star_child_elements:
      for value in desired_rating:
        if int(input.get_attribute('value').split('=')[1]) == value:
          input.find_element(By.XPATH, '..').click()
          
  def sort_by_lowest_price(self):
    self.driver.implicitly_wait(10)
    self.driver.find_element(By.CSS_SELECTOR, 'li[data-id="price"]').click()