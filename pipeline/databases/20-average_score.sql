-- procedure which will calculate average score in User for user

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    -- 1. Declare local variables right at the start
    DECLARE average_score INT;


    -- 2. Calculate average score
    SELECT AVG(score) INTO average_score
    FROM corrections 
    WHERE user_id = user_id;

    -- 3. Update into users
    UPDATE users 
    SET average_score = average_score
    WHERE id = user_id ;
END; //

DELIMITER;
