-- script lists all genres in database by rating

SELECT name, SUM(rate) AS rating FROM tv_genres t1
JOIN tv_show_genres t2 ON t1.id = t2.genre_id
JOIN tv_show_ratings t3 ON t2.show_id = t3.show_id
GROUP BY name
ORDER BY rating DESC;
