from __future__ import print_function

import sys
import psycopg2

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils

def writeToDb(iter):
    for result in iter:
        print(result)
        conn = psycopg2.connect(dbname='pgdb', user='pguser', password='pguser', host='db')
        cur = conn.cursor()

        cur.execute("INSERT INTO event_statistics (product_id, views, purchases, revenue, timestamp) VALUES (%s, %s, %s, %s, NOW())", (result['product_id'],result['views'],result['purchases'], result['revenue']))
        conn.commit()
        conn.close()

def test(pair):
    result = {
        'product_id': pair[0],
        'revenue': 0.0,
        'purchases': 0,
        'views': 0
    }
    for it in pair[1]:
        result['revenue'] += float(it['revenue'])
        if it['type'] == 'view':
            result['views'] += 1
        else:
            result['purchases'] += 1
    print(result)

    return result;

def process(rdd):
    rdd.groupBy(lambda rdd: rdd['product_id']).map(test).foreachPartition(writeToDb)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: flume_wordcount.py <hostname> <port>", file=sys.stderr)
        sys.exit(-1)

    sc = SparkContext(appName="PythonStreamingFlume")
    sc.setLogLevel('ERROR')

    ssc = StreamingContext(sc, 1)

    hostname, port = sys.argv[1:]
    print('Start listening at {}:{}'.format(hostname, port))
    kvs = FlumeUtils.createStream(ssc, hostname, int(port))

    kvs.map(lambda x: x[0]).window(60, 10).foreachRDD(process)

    ssc.start()
ssc.awaitTermination()
