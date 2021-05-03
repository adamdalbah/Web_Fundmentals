SELECT film.title, film.description, film.release_year, film.rating, film.special_features
, category.name as genre, actor.first_name , actor.last_name FROM film
JOIN
 