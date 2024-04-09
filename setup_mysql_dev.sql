-- Créer la base de données "hbnb_dev_db" si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Créer l'utilisateur "hbnb_dev" s'il n'existe pas, avec le mot de passe "hbnb_dev_pwd"
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Accorder tous les privilèges sur la base de données "hbnb_dev_db" à l'utilisateur "hbnb_dev"
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Accorder le privilège SELECT (comme SELECT, INSERT, UPDATE, DELETE, etc.) sur
-- la base de données "performance_schema" à l'utilisateur "hbnb_dev"
-- "performance_schema" est une base de données système qui est créée par défaut dans les installations MySQL
-- utilisée par MySQL pour stocker des métadonnées sur les performances du serveur et les événements internes du serveur
-- par défaut les nouveaux utilisateurs n'y ont aucun privilège.
-- est principalement destiné aux utilisateurs avancés et aux administrateurs système
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
