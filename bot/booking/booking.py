from selenium import webdriver
import selenium
import booking.constants as const
import os
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException     

class Booking(webdriver.Chrome):
  def __init__(self, driver_path = r'../../chromedriver.exe', teardown = False):
    self.driver_path = driver_path
    self.teardown = teardown
    os.environ['PATH'] += self.driver_path
    super(Booking, self).__init__()
    self.implicitly_wait(15)
    self.maximize_window()
    
  # automatic exit with context manager
  def __exit__(self, exc_type, exc_val, exc_tb):
    if self.teardown:
      self.quit()
  
    
  def land_first_page(self):
    self.get(const.BASE_URL)
    
  def change_currency(self, currency = "USD"):
    self.implicitly_wait(const.MINIMUM_WAIT)
    self.find_element(By.CSS_SELECTOR, "button[data-modal-header-async-type='currencyDesktop']").click()
    self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]').click()
    
  def select_target_destination(self, destination):
    search_field = self.find_element(By.ID, 'ss')
    search_field.clear()
    search_field.send_keys(destination)
    first_element_in_list = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
    first_element_in_list.click()
    
  def select_dates(self, check_in_date, check_out_date):
    check_in = check_in_date.split('-')
    check_out = check_out_date.split('-')
      
    self.skip_to_year(check_in[0])
    self.skip_to_month(check_in[1])
    check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
    check_in_element.click()
    
    self.skip_to_year(check_out[0])
    self.skip_to_month(check_out[1])
    check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
    check_out_element.click()
    
  def skip_to_year(self, year):
    next_button = self.find_element(By.CSS_SELECTOR, 'div[data-bui-ref="calendar-next"]')
    while year != self.find_elements(By.CLASS_NAME, 'bui-calendar__month')[0].get_attribute('innerText').split(' ')[1]:
      next_button.click()
      
  def skip_to_month(self, month):
    next_button = self.find_element(By.CSS_SELECTOR, 'div[data-bui-ref="calendar-next"]')
    while month != const.MONTHS[self.find_elements(By.CLASS_NAME, 'bui-calendar__month')[0].get_attribute('innerText').split(' ')[0]]:
      next_button.click()