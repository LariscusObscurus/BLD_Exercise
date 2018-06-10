FROM debian:stretch

RUN set -x && \
    apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install requests && \
    pip3 install psycopg2

COPY monitor.py /monitor.py
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]