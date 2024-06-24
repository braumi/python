# -- Step 1: Create the database
# CREATE DATABASE gta_database;

# -- Step 2: Use the database
# USE gta_database;

# -- Step 3: Create the gta table
# CREATE TABLE gta (
#     game_id INT AUTO_INCREMENT PRIMARY KEY,
#     release_year INT,
#     title VARCHAR(255),
#     city_name VARCHAR(255)
# );

# -- Step 4: Insert data into the gta table
# INSERT INTO gta (release_year, title, city_name) VALUES
# (1997, 'GTA', 'New Guernsey'),
# (1999, 'GTA', 'USA'),
# (2001, 'GTA III', 'Liberty City'),
# (2002, 'GTA: Vice City', 'Vice City'),
# (2004, 'GTA: San Andreas', 'San Andreas'),
# (2008, 'GTA IV', 'Liberty City');

# -- Step 5: Create the cities table
# CREATE TABLE cities (
#     city_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     real_world_counterpart VARCHAR(255)
# );

# -- Step 6: Insert data into the cities table
# INSERT INTO cities (name, real_world_counterpart) VALUES
# ('Liberty City', 'New York');

# -- Step 7: Update the data in both tables
# UPDATE gta
# SET city_name = 'New York'
# WHERE city_name = 'Liberty City';

# UPDATE cities
# SET name = 'New York'
# WHERE name = 'Liberty City';

# -- Step 8: Retrieve and display the results
# SELECT * FROM gta;
# SELECT * FROM cities;
