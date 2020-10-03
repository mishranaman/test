import time
from plyer import notification

if __name__ == '__main__':
     while True:
        notification.notify(
            title="Step away from Laptop",
            message="shift your eyes to look at an object at least 20 feet away, for at least 20 seconds.",
            app_icon="C:\\Users\\naman\\Documents\\Eyes\\k.ico",
            timeout=20,
        )
        time.sleep(20*60)
