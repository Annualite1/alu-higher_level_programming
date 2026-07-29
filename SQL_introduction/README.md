# SQL_introduction

This project covers the fundamentals of SQL and relational databases using MySQL: creating and deleting databases, creating tables, and performing basic CRUD operations, filtering, sorting, and aggregation.

## Learning Objectives

- What's a database
- What's a relational database
- What's SQL, RDBMS, MySQL, ACID, transaction
- How to create a database in MySQL
- How to manage the life cycle of a database
- How to create a table in MySQL
- How to add, delete, update and select data in a table
- How to insert, update or delete rows in a table
- How to use `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`
- What is and how to use aggregate functions like `COUNT` and `AVG`

## Requirements

- All SQL scripts are tested on Ubuntu using MySQL
- Each file should have a comment at the start describing the task
- Scripts run with: `cat <script>.sql | mysql -hlocalhost -uroot -p <database>`

## Files

| File | Description |
| --- | --- |
| `0-list_databases.sql` | Lists all databases of the MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if it doesn't exist |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all tables of a database |
| `4-first_table.sql` | Creates a table `first_table` |
| `5-full_table.sql` | Prints the full description of `first_table` |
| `6-list_values.sql` | Lists all rows of `first_table` |
| `7-insert_value.sql` | Inserts a new row in `first_table` |
| `8-count_89.sql` | Counts records with `id = 89` in `first_table` |
| `9-full_creation.sql` | Creates `second_table` and inserts multiple rows |
| `10-top_score.sql` | Lists all records of `second_table` ordered by score |
| `11-best_score.sql` | Lists records with score >= 10, ordered by score |
| `12-no_cheating.sql` | Updates Bob's score to 10 |
| `13-change_class.sql` | Removes records with score <= 5 |
| `14-average.sql` | Computes the average score |
| `15-groups.sql` | Groups records by score with counts |
| `16-no_link.sql` | Lists records with a name, ordered by score |

## Author

Chouu - ALU Higher Level Programming
