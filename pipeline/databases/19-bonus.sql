-- procedure which will adds a new correction for a student

DELIMITER //

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    -- 1. Declare local variables right at the start
    DECLARE actual_project_id INT;

    -- 2. Insert the project if it doesn't exist yet
    INSERT INTO projects (name)
    SELECT project_name
    WHERE NOT EXISTS (
        SELECT 1 
        FROM projects
        WHERE name = project_name
    );

    -- 3. Find the ID (whether it was just created or already existed)
    SELECT id INTO actual_project_id 
    FROM projects 
    WHERE name = project_name;

    -- 4. Insert into corrections
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, actual_project_id, score);
END; //

DELIMITER;
