#!/usr/bin/env python3

from youtube_dl import MaxDownloadsReached
from common import download


def main():
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
