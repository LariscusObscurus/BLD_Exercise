#!/bin/bash
echo "Starting flume agent"
exec /usr/local/flume/bin/flume-ng agent -c /usr/local/flume/conf -f /usr/local/flume/conf/flume.conf -n agent