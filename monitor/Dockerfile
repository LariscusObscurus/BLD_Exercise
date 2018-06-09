FROM debian:stretch

RUN set -x && \
    apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install requests

COPY monitor.py /monitor.py
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]