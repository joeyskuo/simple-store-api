CREATE TABLE IF NOT EXISTS items (id serial PRIMARY KEY, name text, price real, store_id integer);
CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, username text, password text);
CREATE TABLE IF NOT EXISTS stores (id serial PRIMARY KEY, name text);