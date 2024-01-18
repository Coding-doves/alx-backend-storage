-- SQL script that creates a stored procedure AddBonus

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(
        IN user_id INT,
        IN project_name VARCHAR,
        IN score FLOAT
)
BEGIN
END$$
DELIMITER ;

