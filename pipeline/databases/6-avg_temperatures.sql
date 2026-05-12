-- displayes avg temperatures by city orderd by temperatures

SELECT city, avg(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
