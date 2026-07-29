# SQL_more_queries

This project covers more advanced SQL concepts using MySQL: user management and privileges, table constraints (NOT NULL, DEFAULT, UNIQUE, PRIMARY KEY, FOREIGN KEY), subqueries, JOINs (INNER and LEFT), and aggregate functions with GROUP BY.

## Learning Objectives

- How to create a new MySQL user
- How to manage privileges for a MySQL user
- What's a PRIMARY KEY
- What's a FOREIGN KEY
- What's the main differences between `INNER`, `LEFT` and `RIGHT` JOIN
- How to use `NOT NULL`, `UNIQUE`, `DEFAULT` constraints
- How to use subqueries
- How to use `GROUP BY` and aggregate functions

## Requirements

- All SQL scripts are tested on Ubuntu using MySQL
- Each file should have a comment at the start describing the task
- Scripts run with: `cat <script>.sql | mysql -hlocalhost -uroot -p <database>`

## Files

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists privileges of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates `hbtn_0d_2` and `user_0d_2` with SELECT only |
| `3-force_name.sql` | Creates table `force_name` with `name` NOT NULL |
| `4-never_empty.sql` | Creates table `id_not_null` with `id` defaulting to 1 |
| `5-unique_id.sql` | Creates table `unique_id` with `id` defaulting to 1 and UNIQUE |
| `6-states.sql` | Creates database `hbtn_0d_usa` and table `states` |
| `7-cities.sql` | Creates table `cities` with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Lists cities of California using a subquery |
| `9-cities_by_state_join.sql` | Lists cities with their state name using JOIN |
| `10-genre_id_by_show.sql` | Lists shows with at least one genre linked |
| `11-genre_id_all_shows.sql` | Lists all shows with genre_id, NULL if none |
| `12-no_genre.sql` | Lists shows without a genre linked |
| `13-count_shows_by_genre.sql` | Counts shows linked to each genre |
| `14-my_genres.sql` | Lists all genres of the show Dexter |
| `15-comedy_only.sql` | Lists all Comedy shows |
| `16-shows_by_genre.sql` | Lists all shows and their linked genres |

## Author

Chouu - ALU Higher Level Programming
