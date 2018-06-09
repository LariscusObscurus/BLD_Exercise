FROM debian:stretch

WORKDIR /data

RUN set -x && \
    apt-get update && apt-get install -y curl sudo gnupg software-properties-common

#Install Postgres 10
RUN curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - && \
    add-apt-repository "deb [arch=amd64] http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" && \
    apt-get update && apt-get install -y postgresql-10

#Create Postgres user
USER postgres
RUN /etc/init.d/postgresql start && \
    psql --command "CREATE USER pguser WITH SUPERUSER PASSWORD 'pguser';" && \
    createdb -O pguser pgdb

USER root
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/10/main/pg_hba.conf
#Maybe use conf.d directory instead?
RUN echo "listen_addresses='*'" >> /etc/postgresql/10/main/postgresql.conf 

EXPOSE 5432

RUN mkdir -p /var/run/postgresql && \
    chown -R postgres /var/run/postgresql

#Allow persistence of configs, logs and the database itself
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER postgres
ENTRYPOINT ["/entrypoint.sh"]