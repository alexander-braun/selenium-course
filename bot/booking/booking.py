from selenium import webdriver
import booking.constants as const
import os

class Booking(webdriver.Chrome):
  def __init__(self, driver_path = r'../../chromedriver.exe'):
    self.driver_path = driver_path
    os.environ['PATH'] += self.driver_path
    super(Booking, self).__init__()
    
  def land_first_page(self):
    self.get(const.BASE_URL)
    
