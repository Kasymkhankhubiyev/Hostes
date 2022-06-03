CREATE TABLE people(
id INTEGER PRIMARY KEY,
user_name TEXT NOT NULL,
user_secondname TEXT NOT NULL,
user_iid INTEGER NOT NULL UNIQUE,
user_login TEXT UNIQUE,
user_password TEXT,
user_access_level INTEGER DEFAULT 0 NOT NULL CHECK(0, 1, 2))
