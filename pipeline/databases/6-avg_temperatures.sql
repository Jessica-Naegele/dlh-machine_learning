-- displayes avg temperatures by city orderd by temperatures

SELECT city, avg(value) AS avg_temp FROM hbtn_0c_0.temperatures
GROUP BY city
ORDER BY avg_temp DESC;
