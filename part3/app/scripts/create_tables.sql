
DROP TABLE IF EXISTS place_amenity;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS amenity;
DROP TABLE IF EXISTS users;


CREATE TABLE users (
    id CHAR(36) PRIMARY KEY, 
    first_name VARCHAR(255) NOT NULL, 
    last_name VARCHAR(255) NOT NULL, 
    email VARCHAR(255) UNIQUE NOT NULL, 
    password VARCHAR(255) NOT NULL, 
    is_admin BOOLEAN DEFAULT FALSE
);


CREATE TABLE place (
    id CHAR(36) PRIMARY KEY, 
    title VARCHAR(255) NOT NULL, 
    description TEXT, 
    price DECIMAL(10,2) NOT NULL, 
    latitude FLOAT, 
    longitude FLOAT, 
    owner_id CHAR(36) NOT NULL, 
    FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
);


CREATE TABLE review (
    id CHAR(36) PRIMARY KEY, 
    text TEXT NOT NULL, 
    rating INT CHECK (rating BETWEEN 1 AND 5) NOT NULL, 
    user_id CHAR(36) NOT NULL, 
    place_id CHAR(36) NOT NULL, 
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES place(id) ON DELETE CASCADE,
    CONSTRAINT unique_user_place_review UNIQUE (user_id, place_id)
);


CREATE TABLE amenity (
    id CHAR(36) PRIMARY KEY, 
    name VARCHAR(255) UNIQUE NOT NULL
);


CREATE TABLE place_amenity (
    place_id CHAR(36) NOT NULL, 
    amenity_id CHAR(36) NOT NULL, 
    PRIMARY KEY (place_id, amenity_id), 
    FOREIGN KEY (place_id) REFERENCES place(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenity(id) ON DELETE CASCADE
);


INSERT INTO users (id, first_name, last_name, email, password, is_admin) 
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1', 
    'Admin', 
    'HBnB', 
    'admin@hbnb.io', 
    '$2b$12$y6wM5KtUXxHF/N8T7xLoqOfjOCp6cFJ8HzJ9O2gjJpNqF6R76Q6p2', 
    TRUE
);


INSERT INTO amenity (id, name) VALUES
    (UUID(), 'WiFi'),
    (UUID(), 'Swimming Pool'),
    (UUID(), 'Air Conditioning');


SELECT * FROM users;
SELECT * FROM amenity;
