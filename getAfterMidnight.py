#!/usr/bin/env python3

from datetime import datetime, time, timedelta
from youtube_dl import MaxDownloadsReached
from common import countdown, get_next_midnight, download


def main():
    if datetime.now().time() >= time(hour=5, minute=59):
        # Night owl time has passed. We need to wait for the next midnight.
        print("Waiting until 10 minutes after midnight…")
        countdown(get_next_midnight() + timedelta(minutes=10))

    # User name and password can be none if we have cookies.
    #user_name = "user@example.com"
    #password = getpass.getpass(f"Password for {user_name}: ")
    user_name = None
    password = None

    try:
        download("240", 10, user_name, password)
    except MaxDownloadsReached:
        pass


if __name__ == '__main__':
    main()
