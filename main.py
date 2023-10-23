import time

from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify (
            title = "Study Time",
            message = "You have exam tomorrow so you need to study right now",
            app_icon = r"C:\Users\User\Documents\python\Reaminder\icon.ico",
            timeout = 5
        )
        time.sleep(60*60)
