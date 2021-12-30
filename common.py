from datetime import datetime, timedelta, time
from time import sleep

import youtube_dl


def countdown(until_time: datetime):
    while True:
        diff = until_time - datetime.today()
        if diff <= timedelta(seconds=1):
            # 1 second or less remaining.
            # Sleep exactly the amount of time remaining.
            sleep(max(0., diff.total_seconds()))
            print("Done")
            return
        elif diff <= timedelta(seconds=10):
            # 10 seconds or less remaining. Show every second.
            print(f"{diff.seconds:.1f}s remaining")
            sleep(1)
        elif diff <= timedelta(minutes=1):
            # 1 minute or less remaining. Show every 10 seconds.
            print(f"{diff.seconds:.1f}s remaining")
            sleep(10)
        elif diff <= timedelta(minutes=10):
            # 10 minutes or less remaining. Show every minute.
            print(f"{diff.seconds/60:.1f} min remaining")
            sleep(60)
        elif diff <= timedelta(hours=1):
            # 1 hour or less remaining. Show every 10 minutes.
            print(f"{diff.seconds/60:.1f} min remaining")
            sleep(600)
        else:
            # More than 1 hour remaining. Show every hour.
            print(f"{diff.seconds/3600:.1f} hours remaining")
            sleep(3600)


def get_next_midnight() -> datetime:
    now = datetime.today()
    tomorrow = now + timedelta(days=1)
    midnight = datetime.combine(tomorrow, time(0, 0, 0))
    return midnight


def download(max_height, n, user_name, password):
    with youtube_dl.YoutubeDL({
        'username': user_name,
        'password': password,
        'format': f"bestvideo[height<={max_height}]+bestaudio/best[height<={max_height}]",
        'max_downloads': n,
        'mark_watched': True,
        'download_archive': "archive.txt",
        'cookiefile': "cookies.txt",
        'outtmpl': "downloaded/%(upload_date)s - %(uploader)s - %(title)s - %(id)s.%(ext)s",
        'playlistreverse': False,
        'ignore_errors': True,
        'embedsubtitles': True,
        'writesubtitles': True,
        # 'simulate': True,
    }) as ydl:
        ydl.download([":ytwatchlater"])
