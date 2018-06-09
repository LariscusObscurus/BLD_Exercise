CREATE TABLE IF NOT EXISTS event_statistics (
    id serial primary key,
    product_id int not null,
    views int not null,
    purchases int not null,
    revenue int not null,
    timestamp timestamp not null
);