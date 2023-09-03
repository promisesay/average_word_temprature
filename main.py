import requests
import sqlite3
import selectorlib
from datetime import datetime
import time

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
databass = sqlite3.connect("databass.db")

response = requests.get(URL)
data = response.text


def select(source):
    fo = selectorlib.Extractor.from_yaml_file("extract.yaml")
    receive = fo.extract(source)["home"]
    return receive


def store(temp):
    time = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = databass.cursor()
    cursor.execute("INSERT INTO events VALUES (?,?)", (temp, time))
    databass.commit()


if __name__ == "__main__":
    while True:
        extract = select(data)
        store(extract)
        time.sleep(3)

