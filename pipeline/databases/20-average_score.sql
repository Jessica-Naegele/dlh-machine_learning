-- procedure which will calculate average score in User for user

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    -- 1. Declare local variables right at the start
    DECLARE calc_avg INT;


    -- 2. Calculate average score
    SELECT AVG(score) INTO calc_avg
    FROM corrections t2
    WHERE t2.user_id = user_id;

    -- 3. Update into users
    UPDATE users
    SET average_score = calc_avg
    WHERE id = user_id ;
END; //

DELIMITER;
