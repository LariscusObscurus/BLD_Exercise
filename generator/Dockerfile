FROM debian:stretch

RUN set -x && \
    apt-get update && \
    apt-get install -y python3

COPY EventGenerator.py /generator/EventGenerator.py
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /generator/EventGenerator.py
ENTRYPOINT ["/entrypoint.sh"]