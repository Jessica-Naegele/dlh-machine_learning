SELECT * FROM users;
SELECT * FROM corrections;

#drop Procedure ComputeAverageScoreForUser;

SELECT "--";
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

SELECT "--";
SELECT * FROM users;