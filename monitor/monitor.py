#!/usr/bin/python3 -u
import psycopg2
import time
import sys
import pprint

time.sleep(30)

conn = psycopg2.connect(dbname='pgdb', user='pguser', password='pguser', host='db')
cur = conn.cursor()

while True:
    cur.execute("select * from event_statistics where timestamp > CURRENT_TIMESTAMP - INTERVAL '1 minutes'")
    results = cur.fetchall()
    pprint.pprint(results)
    sys.stdout.flush()
    time.sleep(10)

conn.close()
