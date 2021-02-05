"""A vaccination calculator."""

__author__ = "730392685"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: ")

doses_administered: int = int(input("Doses administered: "))

doses_per_day: int = int(input("Doses per day: "))

target_percentage_vaccinated: int(input("Target percentage vaccinated: "))

target_vaccination_population: float = (target_percentage_vaccinated / 100) * population

people_left_to_be_vaccinated: int = target_vaccination_population - (doses_administered / 2)

doses_needed_to_vaccinate_them: int = 2 * people_left_to_be_vaccinated 

days: int = doses_needed_to_vaccinate_them / doses_per_day

today: datetime = datetime.today()

days_time: timedelta = timedelta(int(days))

future: datetime = today + days_time

print("We will reach " + target_percentage_vaccinated + "% vaccination in " + days + "days, which falls on " + future.strftime("%B %d, %Y")