from booking.booking import Booking


with Booking() as bot:
  bot.land_first_page()
  bot.click_cookie_banner_accept()
  bot.change_currency(currency="EUR")
  bot.select_target_destination("Fidschi")
  bot.select_dates(check_in_date="2022-12-01", check_out_date="2023-01-12")
  bot.select_guests(adults=3, children=2, rooms=2, children_ages=[3, 4])
  bot.click_search()
  bot.apply_filtrations(3, 4, 5, 6)