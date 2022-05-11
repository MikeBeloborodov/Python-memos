from win10toast import ToastNotifier
import datetime
import time

toaster = ToastNotifier()

while True:
    curr_time = datetime.datetime.now()
    current_minute = int(str(curr_time)[14:16])
    toaster.show_toast("Please, stay hydrated",
                "It's important to drink water every hour!",
                icon_path="water.ico",
                duration=10)
    how_much_should_i_sleep = 3600 - current_minute * 60
    time.sleep(how_much_should_i_sleep)
   
