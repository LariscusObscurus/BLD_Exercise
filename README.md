# BLD_Exercise
Exercise Solution for the course big and linked data(BLD)

PostgreSQL, Python, Pyspark where used to create this solution

Generator -> Flume -> Spark -> Db -> Monitor

Spark writes data into the database once per minute.

The output interval of the monitor is five seconds -  the top 10 products (defined by view-count) of the last 5 minutes are printed.

Team:
- Leonhardt Schwarz
- Markus Koller
