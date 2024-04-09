-- Créer la base de données "hbnb_test_db" si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Créer l'utilisateur "hbnb_test" s'il n'existe pas, avec le mot de passe "hbnb_test_pwd"
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Accorder tous les privilèges sur la base de données "hbnb_test_db" à l'utilisateur "hbnb_test"
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Accorder le privilège SELECT sur la base de données "performance_schema" à l'utilisateur "hbnb_test"
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
