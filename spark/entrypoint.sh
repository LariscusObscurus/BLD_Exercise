#!/bin/bash
exec /usr/local/spark/bin/spark-submit --jars /data/spark-streaming-flume-assembly_2.11-2.3.0.jar /spark.py spark 8888