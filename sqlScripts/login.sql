SELECT user_password
FROM people
WHERE user_access_level in (1, 2) AND user_login = ?