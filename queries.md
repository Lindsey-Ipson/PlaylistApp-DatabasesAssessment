Make sure you download the starter code and run the following:

```sh
  psql < movies.sql
  psql movies_db
```

In markdown, you can place a code block inside of three backticks (```) followed by the syntax highlighting you want, for example

\```sql

SELECT \* FROM users;

\```

Using the `movies_db` database, write the correct SQL queries for each of these tasks:

1.  The title of every movie.

        ```sql

    SELECT title FROM movies;

````

2.  All information on the G-rated movies.

	```sql
SELECT * FROM movies WHERE rating = 'G';
````

3.  The title and release year of every movie, ordered with the oldest movie first.
    ```sql
    SELECT title, release_year FROM movies
    ORDER BY release_year;
    ```

````

4.  All information on the 5 longest movies.

	```sql
SELECT * FROM movies
ORDER BY runtime DESC  LIMIT 5;
````

5.  A query that returns the columns of `rating` and `total`, tabulating the total number of G, PG, PG-13, and R-rated movies.
    ```sql
    SELECT \* FROM movies
    ORDER BY runtime DESC LIMIT 5;
    ```

````

6.  A table with columns of `release_year` and `average_runtime`, tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).

	```sql
SELECT release_year, ROUND(AVG(runtime), 0)
as average_runtime
FROM movies GROUP BY release_year
ORDER BY release_year DESC;
````

7.  The movie title and studio name for every movie in the database.

        ```sql

    SELECT title, name FROM movies
    INNER JOIN studios ON studio_id = studios.id;

````

8.  The star first name, star last name, and movie title for every matching movie and star pair in the database.

	```sql
SELECT first_name, last_name, title
FROM movies
JOIN roles ON movies.id = movie_id
JOIN stars ON star_id = stars.id;
````

9.  The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. _IMPORTANT NOTE_: it's possible that there can be two _different_ actors with the same name, so make sure your solution accounts for that.

        ```sql

    SELECT DISTINCT first_name, last_name
    FROM movies
    JOIN roles ON movies.id = movie_id
    JOIN stars ON star_id = stars.id
    WHERE rating = 'G';
    ;

````

10. The first and last names of every star along with the number of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure that two different actors with the same name are considered separately).

 	```sql
SELECT DISTINCT first_name, last_name,
COUNT(DISTINCT movies.id) as total_movies
FROM movies
JOIN roles ON movies.id = movie_id
JOIN stars ON star_id = stars.id
GROUP BY first_name, last_name
ORDER BY total_movies DESC;
````

### The rest of these are bonuses

11. The title of every movie along with the number of stars in that movie, in descending order by the number of stars.
    ```sql
    SELECT movies.title, COUNT(DISTINCT stars.id) as star_count
    FROM movies
    JOIN roles ON movies.id = roles.movie_id
    JOIN stars ON roles.star_id = stars.id
    GROUP BY movies.id, movies.title
    ORDER BY star_count DESC;
    ```

````

12. The first name, last name, and average runtime of the five stars whose movies have the longest average.

    ```sql
SELECT stars.first_name, stars.last_name,
ROUND(AVG(movies.runtime), 0) as average_runtime
FROM stars
JOIN roles ON stars.id = roles.star_id
JOIN movies ON roles.movie_id = movies.id
GROUP BY stars.id, stars.first_name, stars.last_name
ORDER BY average_runtime DESC
LIMIT 5;
````

13. The first name, last name, and average runtime of the five stars whose movies have the longest average, among stars who have more than one movie in the database.
    ```sql
    SELECT stars.first_name, stars.last_name, ROUND(AVG(movies.runtime), 0) as average_runtime
    FROM stars
    JOIN roles ON stars.id = roles.star_id
    JOIN movies ON roles.movie_id = movies.id
    GROUP BY stars.id, stars.first_name, stars.last_name
    HAVING COUNT(DISTINCT movies.id) > 1
    ORDER BY average_runtime DESC
    LIMIT 5;
    ```

````

14. The titles of all movies that don't feature any stars in our database.

    ```sql
SELECT title
FROM movies
WHERE id NOT IN (
  SELECT DISTINCT movie_id
  FROM roles
);
````

15. The first and last names of all stars that don't appear in any movies in our database.

        ```sql

    SELECT first_name, last_name
    FROM stars
    WHERE id NOT IN (
    SELECT DISTINCT star_id
    FROM roles
    );

````

16. The first names, last names, and titles corresponding to every role in the database, along with every movie title that doesn't have a star, and the first and last names of every star not in a movie.

    ```sql
SELECT stars.first_name, stars.last_name, movies.title
FROM roles
RIGHT JOIN movies ON roles.movie_id = movies.id
RIGHT JOIN stars ON roles.star_id = stars.id
UNION
SELECT NULL AS first_name, NULL AS last_name, movies.title
FROM movies
LEFT JOIN roles ON movies.id = roles.movie_id
WHERE roles.movie_id IS NULL
UNION
SELECT stars.first_name, stars.last_name, NULL AS title
FROM stars
LEFT JOIN roles ON stars.id = roles.star_id
WHERE roles.star_id IS NULL;
````
