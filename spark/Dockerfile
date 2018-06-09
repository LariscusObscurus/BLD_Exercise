FROM debian:stretch

RUN set -x && \
    apt-get update && apt-get install -y python3 wget openjdk-8-jdk python

WORKDIR /data

RUN mkdir /usr/local/spark && \
    wget http://mirror.klaus-uwe.me/apache/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz  && \
    tar xzvf spark-2.3.0-bin-hadoop2.7.tgz -C /usr/local/spark --strip-components=1

#Add spark-submit to PATH
RUN export PATH=$PATH:/usr/local/spark/bin

COPY spark.py /spark.py

ENTRYPOINT [ "/bin/bash" ]