-- script shows all shows wtih tv_show.title, tv_show_genres.genre_id, 

SELECT title AS title, genre_id as genre_id FROM tv_shows, tv_show_genres
WHERE hbtn_0d_tvshows.tv_shows.id = hbtn_0d_tvshows.tv_show_genres.show_id
ORDER BY title, genre_id asc;
