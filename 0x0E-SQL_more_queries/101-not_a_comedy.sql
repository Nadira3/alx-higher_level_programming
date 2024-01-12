-- lists all shows from hbtn_0d_tvshows_rate by their rating.

	-- Each record should display: tv_shows.title - rating sum
	-- Results must be sorted in descending order by the rating
	-- You can use only one SELECT statement
	-- The database name will be passed as an argument of the mysql command

SELECT title FROM tv_shows
	WHERE title NOT IN
		(SELECT tv_shows.title
		FROM tv_shows
		JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
		JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id 
		WHERE tv_genres.name = 'Comedy')
	ORDER BY tv_shows.title ASC
;
