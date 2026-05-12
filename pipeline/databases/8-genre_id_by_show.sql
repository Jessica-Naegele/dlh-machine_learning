-- script shows all shows wtih tv_show.title, tv_show_genres.genre_id, 

SELECT title AS title, genre_id AS genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id ASC;
