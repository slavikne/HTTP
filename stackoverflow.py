import requests
from pprint import pprint
import datetime

API_BASE_URL = "https://api.stackexchange.com/2.3/questions"
headers = {
     'Accept': 'application/json',
 }
today = datetime.datetime.today()
second = today.timestamp()
response = requests.get(API_BASE_URL, params={'tagged': "Python", 'site': 'stackoverflow', 'fromdate': f'{int(second) - 259200}', 'todate': f'{int(second)}'},
                        headers=headers)
for question in response.json()['items']:
    pprint(question['title'])