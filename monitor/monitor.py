#!/usr/bin/python3 -u
import psycopg2
import time
import sys
import pprint

time.sleep(20)

conn = psycopg2.connect(dbname='pgdb', user='pguser', password='pguser', host='db')
cur = conn.cursor()

while True:
    
    cur.execute("select product_id, sum(revenue) as revenue from event_statistics where timestamp > (statement_timestamp() - INTERVAL '5 minutes') group by product_id ORDER BY revenue DESC limit 10")
    if cur.rowcount>0:
        results = cur.fetchall()
        toprint="TOP PRODUKTE (Umsatz) der letzten 5 Minuten\n"
        x=0
        for product_id, revenue in results:
            x+=1
            toprint+=str(x)+". Produkt "+str(product_id)+" ("+str(revenue)+" EUR)\n"
        print(toprint)
        sys.stdout.flush()

    '''
    cur.execute("select product_id, views, event_statistics.timestamp from event_statistics where event_statistics.timestamp > (statement_timestamp() - INTERVAL '1 minutes') ORDER BY event_statistics.timestamp ASC")
    if cur.rowcount>0:
        results = cur.fetchall()
        toprint=""
        for product_id, views, timestamp in results:
            toprint+=str(product_id)+" - "+str(views)+" - "+str(timestamp)+")\n"
        print(toprint)
        sys.stdout.flush()
    '''
    time.sleep(5)

conn.close()
