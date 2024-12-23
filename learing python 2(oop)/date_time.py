#import datetime = this module can provide real time date and time.  It uses the system's local clock to obtain the current date and time.
#Q) check if cs50 2025 is out as of today (dec 12 2024)
import datetime



target_date = datetime.datetime(2025, 1, 1, 12, 00, 00)
now = datetime.datetime.now()   #to find the exact time, the variable name must be "now"

#now = now.strftime("time = %H: %M: %S \n date = %Y-%m-%d")   #   can use this function to edit how we show in the console. But using this doesn't allow comparing two times. So it is commented for now
print (now)


print(".........................................")

if now > target_date:
    print ("CS50 2025 has been updated")
else:
    print ("CS50 has not been updated yet")
    print (f"time left = {target_date - now}")

