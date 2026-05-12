-- without linked genre_id

SELECT title AS title, genre_id FROM tv_shows t1
LEFT JOIN tv_show_genres t2 ON t1.id = t2.show_id
WHERE t2.genre_id IS NULL
ORDER BY title, genre_id ASC;
