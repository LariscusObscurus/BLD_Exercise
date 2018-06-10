#!/usr/bin/python3 -u
import random
import time
import json
import requests

url_flume = 'http://192.168.0.15:{}'
purchases_port = 9999
views_port = 9998

headers = {'content-type': 'application/json'}

while True:
    interval = random.randint(10, 100)
    event_type = 'view' if random.randint(0, 1) else 'purchase'
    revenue = 0 if event_type == 'view' else random.random() * 100

    customerID = random.randint(0, 100000)
    productID = random.randint(0, 100)

    data = {
        'type': event_type,
        'product_id': productID,
        'customer_id': customerID,
        'revenue': revenue,
        'timestamp': time.time(),
    }


    wusa = {
        'headers': data,
        'body': "{}".format(data)
    }
    jsonEvent =  '[{}]'.format(json.dumps(wusa))  
    print(jsonEvent);

    try:
        port_to_use = purchases_port
        response = requests.post(url_flume.format(port_to_use), data=jsonEvent, headers=headers)
        print(response)
    except:
        print("Request failed.")
    time.sleep(1 / interval)
