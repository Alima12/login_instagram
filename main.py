import requests 
from datetime import datetime
import json
from dotenv import load_dotenv
import os
from db import get_db

load_dotenv(".env")
database = get_db()

PASSWORD = os.getenv("password") 
USERNAME = os.getenv("username") 
login_url = 'https://www.instagram.com/accounts/login/ajax/'

def login(username:str, password:str):
    time = int(datetime.now().timestamp())
    csrf = "sfdgdfgdsfgsdfgsd"
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }

    login_response = requests.post(login_url, data=payload, headers=login_header)
    json_data = json.loads(login_response.text)

    if json_data.get("authenticated"):
        print("login successful")
        cookies = login_response.cookies
        cookie_jar = cookies.get_dict()
        database.insert_one(cookie_jar)
    else:
        print("login failed ", login_response.text)

if __name__ == "__main__":
    login(USERNAME, PASSWORD)