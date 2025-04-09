import requests
import json
import logging
from dotenv import load_dotenv
import os
import time

load_dotenv()

logging.basicConfig(filename='error.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
ip = os.getenv("Node_IP")
url = 'http://{}:8888/status'.format(ip)
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.content)
    with open('peers.json', 'w') as f:
        json.dump(data["peers"], f)
        print("Peer data received...")
        print("peers.json file created")

else:
    logging.error('HTTP request failed. Error Code: {}'.format(response.status_code))
