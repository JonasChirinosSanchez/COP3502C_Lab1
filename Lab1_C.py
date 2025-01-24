#Lab1_C

#assume:
# All inputs are valid integers greater than 0
# Years always have exactly 12 months
# Months always have exactly 30 days


yr_date1 = int(input("Enter the year for date 1: "))
month_date1 = int(input("Enter the month for date 1: "))
day_date1 = int(input("Enter the day for date 1: "))
date1 = str(f"{month_date1}/{day_date1}/{yr_date1}")

yr_date2 = int(input("Enter the year for date 2: "))
month_date2 = int(input("Enter the month for date 2: "))
day_date2 = int(input("Enter the day for date 2: "))
date2 = str(f"{month_date2}/{day_date2}/{yr_date2}")

date1_in_days = (((yr_date1)*12)*30) + ((month_date1)*30) + day_date1
date2_in_days = (((yr_date2)*12)*30) + ((month_date2)*30) + day_date2

difference_days = abs(date2_in_days - date1_in_days)

print(f"The difference between {date1} and {date2} is {difference_days} days!")
