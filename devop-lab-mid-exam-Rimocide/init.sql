CREATE TABLE users (
    id SERIAL PRIMARY KEY,             -- Unique identifier for each user
    name VARCHAR(100) NOT NULL,        -- User's name (required)
    email VARCHAR(120) UNIQUE NOT NULL, -- User's email (required, unique)
    phone VARCHAR(15),                 -- Optional phone field
    cnic VARCHAR(13) NOT NULL          -- CNIC field (required, 13 digits)
);
