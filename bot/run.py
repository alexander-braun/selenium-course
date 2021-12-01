from booking.booking import Booking


with Booking() as bot:
  bot.land_first_page()
  bot.change_currency(currency="EUR")
  bot.select_target_destination("Fidschi")
  bot.select_dates(check_in_date="2022-12-01", check_out_date="2023-01-12")
  bot.select_guests(3, 2, 2, [3, 4])