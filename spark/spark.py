import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
#from pyspark.streaming.flume import FlumeUtils

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: network_wordcount.py <hostname> <port>")
        sys.exit(-1)
    sc = SparkContext(appName='PythonStreamingNetworkWordCount')
    sc.setLogLevel('WARN')
   
    ssc = StreamingContext(sc, 1)

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    counts = lines.flatMap(lambda line: line.split(" "))\
                  .map(lambda word: (word, 1))\
                  .reduceByKey(lambda a, b: a+b)
    counts.pprint()

    ssc.start()
    ssc.awaitTermination()