import os
import requests
import time
import csv
import datetime

class Hunter:
    def __init__(self, username):
        self.username = username
        self.writer: csv.DictWriter = None
        self.user_agent = "Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)"
        self.proxy = os.getenv('PROXY')
        self.file = None
        self.start()
        self.loop()

    def start(self):
        self.file = open(f'{self.username}.csv', 'a+', newline='')
        self.writer = csv.DictWriter(self.file, fieldnames=["username", "followers", "following", "date"])
        
        if len(open(f"{self.username}.csv").read()) < 2:
            self.writer.writeheader()

    def get_account_info(self):
        try:
            response = requests.get(
                url=f"https://i.instagram.com/api/v1/users/web_profile_info/?username={self.username}",
                headers={
                    "User-Agent": self.user_agent
                },
                proxies={
                    "https": self.proxy
                }
            )

            if response.status_code == 200:
                json = response.json()

                if json.get('status') != 'ok':
                    raise Exception("Something happened while getting information from Instagram.")
                else:
                    return {
                        "followers": json.get('data').get('user').get('edge_followed_by').get('count'),
                        "following": json.get('data').get('user').get('edge_follow').get('count'),
                        "username": json.get('data').get('user').get('username'),
                        "date": datetime.datetime.now()
                    }
            else:
                raise Exception("Something happened while getting information from Instagram.")
        except Exception as e:
            print(e)

    def loop(self):
        while 1:
            try:
                info = self.get_account_info()
                self.writer.writerow(info)
                self.file.flush()
                print(info)
                time.sleep(60*5)
            except Exception as e:
                print(e)
