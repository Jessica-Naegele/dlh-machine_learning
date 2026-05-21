-- creates stored procedure that computes and store the average score for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    -- 1. Declare local variables right at the start
    DECLARE wgh_avg FLOAT;
    DECLARE wgh INT;

    -- 2. ADD WGH
    SELECT SUM(weight) INTO wgh
    FROM projects t1
    JOIN corrections t2
    ON t1.id = t2.project_id
    WHERE t2.user_id = user_id;

    -- 3. Calc weigted average

    SELECT SUM(score * weight) / wgh INTO wgh_avg
    FROM corrections t2 
    JOIN projects t1 on t1.id = t2.project_id
    WHERE t2.user_id = user_id;

    -- 4. Update into users
    UPDATE users
    SET average_score = wgh_avg
    WHERE id = user_id ;
END; //

DELIMITER ;
