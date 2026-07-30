# python-object_relational_mapping

This project covers Object-Relational Mapping (ORM) in Python: connecting to a MySQL database using `MySQLdb`, protecting against SQL injection, and using SQLAlchemy to map Python classes to database tables.

## Learning Objectives

- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to process results of an SQL query in Python
- How to use format() and `%s`/parameterized queries to sanitize input from users
- What ORM means
- How to map a Python class to a MySQL table using SQLAlchemy
- How to get all objects/some objects/first object of a model from a database
- How to insert, update, and delete objects into a database
- How to use SQLAlchemy sessions

## Requirements

- Uses `MySQLdb` for raw SQL scripts (tasks 0-5)
- Uses `SQLAlchemy` ORM for the rest (tasks 6-14)
- All scripts connect to a MySQL server on `localhost` port `3306`
- All scripts avoid executing on import (`if __name__ == "__main__":`)

## Files

| File | Description |
| --- | --- |
| `0-select_states.py` | Lists all states from `hbtn_0e_0_usa` |
| `1-filter_states.py` | Lists states starting with N |
| `2-my_filter_states.py` | Filters states by user input (unsafe) |
| `3-my_safe_filter_states.py` | Filters states by user input (SQL injection safe) |
| `4-cities_by_state.py` | Lists all cities with their state |
| `5-filter_cities.py` | Lists cities of a given state (SQL injection safe) |
| `model_state.py` | SQLAlchemy `State` model |
| `6-model_state.py` | Creates the `states` table via SQLAlchemy |
| `7-model_state_fetch_all.py` | Lists all `State` objects via SQLAlchemy |
| `8-model_state_fetch_first.py` | Prints the first `State` object |
| `9-model_state_filter_a.py` | Lists all `State` objects containing "a" |
| `10-model_state_my_get.py` | Prints the id of a `State` matching a name |
| `11-model_state_insert.py` | Inserts a new "Louisiana" `State` |
| `12-model_state_update_id_2.py` | Updates the `State` with id 2 |
| `13-model_state_delete_a.py` | Deletes all `State` objects containing "a" |
| `model_city.py` | SQLAlchemy `City` model, linked to `State` |
| `14-model_city_fetch_by_state.py` | Lists all `City` objects with their state |

## Author

Chouu - ALU Higher Level Programming
