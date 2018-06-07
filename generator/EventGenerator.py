#!/usr/bin/python3 -u
import random
import time
import json
import requests

url_flume = 'http://127.0.0.1:80'
headers = {'content-type': 'application/json'}

while True:
    interval = random.randint(10, 100)
    customerID = random.randint(0, 100000)
    productID = random.randint(0, 100)
    revenue = random.random() * 100
    data = {
        'timestamp': time.time(),
        'product_id': productID,
        'customer_id': customerID,
        'revenue': revenue
    }
    jsonEvent = json.dumps(data)

    try:
        response = requests.post(url_flume, data=jsonEvent, headers=headers)
    except:
        print("Request failed.")
        pass
    time.sleep(1 / interval)
