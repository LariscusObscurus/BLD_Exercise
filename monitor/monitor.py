#!/usr/bin/python3 -u
import psycopg2
import time
import sys
import pprint

time.sleep(15)

conn = psycopg2.connect(dbname='pgdb', user='pguser', password='pguser', host='db')
cur = conn.cursor()

while True:
    cur.execute("select product_id, views from event_statistics where timestamp > CURRENT_TIMESTAMP - INTERVAL '5 minutes' ORDER BY views DESC")
    if cur.rowcount>0:
        results = cur.fetchall()
        toprint="TOP PRODUKTE (Views) der letzten 5 Minuten\n"
        for x in range(1, 11):
            if x<len(results):
                toprint+=str(x)+". "+str(results[x][0])+"("+str(results[x][1])+")\n"
        print(toprint)
        sys.stdout.flush()
    time.sleep(5)

conn.close()
