from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils

def test(x):
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
    print("x")
    print(x)
    print("x0")
    print(x[0])
    print("x1")
    print(x[1])
    return x[1];

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: flume_wordcount.py <hostname> <port>", file=sys.stderr)
        sys.exit(-1)

    sc = SparkContext(appName="PythonStreamingFlumeWordCount")
    sc.setLogLevel('ERROR')

    ssc = StreamingContext(sc, 1)

    hostname, port = sys.argv[1:]
    kvs = FlumeUtils.createStream(ssc, hostname, int(port))

    lines = kvs.map(test)
    counts = lines.flatMap(lambda line: line.split(" ")) \
       .map(lambda word: (word, 1)) \
       .reduceByKey(lambda a, b: a+b)
    counts.pprint()

    ssc.start()
ssc.awaitTermination()
