-- display max temperatures per states

SELECT state, MAX(value) as max_temp FROM hbtn_0c_0.temperatures
GROUP BY state
ORDER BY state;