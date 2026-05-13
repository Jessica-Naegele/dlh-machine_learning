-- Active: 1778347204990@@localhost@3306@hbtn_0d_tvshows_rates
-- script that lists all shows by their rating

SELECT title, SUM(rate) AS rating FROM tv_shows t1
JOIN tv_show_ratings t2 ON t1.id = t2.show_id
GROUP BY title
ORDER BY rating DESC;
