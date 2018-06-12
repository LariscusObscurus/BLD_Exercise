FROM debian:stretch

RUN set -x && \
    apt-get update && apt-get install -y python3 wget openjdk-8-jdk-headless python

WORKDIR /data

RUN mkdir /usr/local/spark && \
    wget http://mirror.klaus-uwe.me/apache/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz  && \
    tar xzvf spark-2.3.0-bin-hadoop2.7.tgz -C /usr/local/spark --strip-components=1

RUN wget http://central.maven.org/maven2/org/apache/spark/spark-streaming-flume-assembly_2.11/2.3.0/spark-streaming-flume-assembly_2.11-2.3.0.jar

RUN apt-get install -y python-pip && pip install psycopg2

EXPOSE 8888

#Add spark-submit to PATH
RUN export PATH=$PATH:/usr/local/spark/bin

COPY spark.py /spark.py
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
