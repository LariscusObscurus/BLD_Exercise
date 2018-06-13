# BLD_Exercise
Exercise Solution for the course big and linked data(BLD)

PostgreSQL, Python, Pyspark where used to create this solution

Generator -> Flume -> Spark -> Db -> Monitor

Spark writes data into the database once per minute.

The output interval of the monitor is five seconds -  the top 10 products of the last 5 minutes are printed.
There is no (monitor-)output for the first 60 seconds since Spark writes into the database every minute.

Build: docker-compose build
Run: docker-compose up

Tested in: Debian 9(native), Debian 9(HyperV), Scaleway (scaleway.com)

Team:
- Leonhardt Schwarz
- Markus Koller
