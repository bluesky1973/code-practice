import time
from plyer import notification

if __name__ == "_main_":
    while True:
        notification.notify(
            title = "Alert!",
            message = "Take a break! it has been an hour!",
            timeout = 10
        )
        time.sleep(3600)