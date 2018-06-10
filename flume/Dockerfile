FROM debian:stretch

RUN set -x && \
    apt-get update && apt-get install -y wget openjdk-8-jdk

WORKDIR /data

RUN mkdir /usr/local/flume && \
    wget http://archive.apache.org/dist/flume/1.8.0/apache-flume-1.8.0-bin.tar.gz  \
    && tar xzvf apache-flume-1.8.0-bin.tar.gz -C /usr/local/flume --strip-components=1

EXPOSE 9999

COPY flume.conf /usr/local/flume/conf/flume.conf
COPY flume-env.sh /usr/local/flume/conf/flume-env.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]