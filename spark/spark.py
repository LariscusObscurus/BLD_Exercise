from __future__ import print_function

import sys
import psycopg2

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils


def test(pair):
    result = {
        'product_id': pair[0],
        'revenue': 0.0,
    }
    for it in pair[1]:
        result['revenue'] += float(it['revenue'])
    print(result)

    conn = psycopg2.connect(dbname='pgdb', user='pguser', password='pguser', host='192.168.0.15')
    cur = conn.cursor()

    # Hello SQL injection 
    cur.execute("INSERT INTO event_statistics (product_id, views, purchases, revenue, timestamp) VALUES (%s, 1, 1, %s, NOW())", (result['product_id'], result['revenue']))
    conn.commit()
    conn.close()
    return result;

def process(rdd):
    result = rdd.groupBy(lambda rdd: rdd['product_id']).map(test)
    result.collect()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: flume_wordcount.py <hostname> <port>", file=sys.stderr)
        sys.exit(-1)

    sc = SparkContext(appName="PythonStreamingFlumeWordCount")
    sc.setLogLevel('ERROR')

    ssc = StreamingContext(sc, 1)

    hostname, port = sys.argv[1:]
    kvs = FlumeUtils.createStream(ssc, hostname, int(port))

    kvs.map(lambda x: x[0]).window(60, 10).foreachRDD(process)

    ssc.start()
ssc.awaitTermination()
