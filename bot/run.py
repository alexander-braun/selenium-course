from booking.booking import Booking
from selenium.common.exceptions import WebDriverException

# from terminal:
# set PATH "C:\Users\Alex\Desktop\Apps\web_scraping_selenium;%PATH%"
# python run.py

try:
  with Booking() as bot:
    bot.land_first_page()
    bot.click_cookie_banner_accept()
    bot.change_currency(currency="EUR")
    bot.select_target_destination(input("Where to? "))
    check_in_date = input("Check in date (format: YYYY-MM-DD): ")
    check_out_date = input("Check out date (format: YYYY-MM-DD): ")
    bot.select_dates(check_in_date=check_in_date, check_out_date=check_out_date)
    adults = int(input("How many adults? "))
    children = int(input("How many children? "))
    children_ages = []
    if (children > 0):
      for i in range(children):
        children_ages.append(input(f"Child {i + 1} age: "))
    rooms = int(input("How many rooms? "))
    bot.select_guests(adults=adults, children=children, rooms=rooms, children_ages=children_ages)
    bot.click_search()
    star_selection = input("Comma seperated list of number of stars the hotel should have: ")
    stars = star_selection.split(',')
    for i in range(len(stars)):
      stars[i] = int(stars[i])
    bot.apply_filtrations(*stars)
    bot.refresh()
    bot.report_results()
except WebDriverException as e:
  print(
    e,
    'You are trying to run the bot from the command line\n'
    'Please add to PATH your Selenium Drivers\n\n'
    'Windows: \n'
    'set PATH=%PATH;C:path-to-your-folder \n\n'
    'Linux: \n'
    'PATH=/path/to/your/folder \n'
  )
except Exception as e:
  print("Exception!",e)