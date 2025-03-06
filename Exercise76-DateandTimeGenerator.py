# please print the script in the excepted output
# example: Today is Wednesday, December 28, 2016

from datetime import datetime

print(datetime.now().strftime("Today is %A, %B %d, %Y"))
