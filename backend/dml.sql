CREATE TABLE categories (category_name VARCHAR(100) PRIMARY KEY, last_updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
CREATE TABLE conferences (conf_name VARCHAR(100) PRIMARY KEY, location VARCHAR(100), lat FLOAT, lng FLOAT, link TEXT, deadline VARCHAR(25));
CREATE TABLE categories_conferences (category VARCHAR(100) NOT NULL, conference VARCHAR(100) NOT NULL, FOREIGN KEY (category) REFERENCES categories(category_name), FOREIGN KEY (conference) REFERENCES conferences(conf_name));