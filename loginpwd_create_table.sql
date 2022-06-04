CREATE TABLE people(
user_id INTEGER PRIMARY KEY,
user_name TEXT NOT NULL,
user_secondname TEXT NOT NULL,
user_iid TEXT NOT NULL UNIQUE,
user_login TEXT UNIQUE,
user_password TEXT,
user_access_level INTEGER DEFAULT 0 NOT NULL,
user_email TEXT,
user_phone_number TEXT NOT NULL
)
