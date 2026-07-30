# python-almost_a_circle

This project builds up a small class hierarchy in Python (`Base`, `Rectangle`, `Square`), covering private attributes, getters/setters, inheritance, class/static methods, JSON serialization, and unit testing.

## Learning Objectives

- Why Python programming is awesome
- Unittest concept and how to write unit tests
- How to use `*args` and `**kwargs`
- How to handle `**kwargs` in your `update` method
- How to serialize and deserialize a Class
- How to write and read a JSON file
- Class, static, and instance methods
- Args and kwargs

## Project Structure
## Classes

- **`Base`**: Manages the `id` attribute for all subclasses. Includes
  `to_json_string`, `save_to_file`, `from_json_string`, `create`, and
  `load_from_file` for JSON serialization/deserialization.
- **`Rectangle`** (inherits from `Base`): Has private attributes
  `width`, `height`, `x`, `y` with validated getters/setters, plus
  `area`, `display`, `__str__`, `update`, and `to_dictionary`.
- **`Square`** (inherits from `Rectangle`): Has a `size` getter/setter
  that maps to `width` and `height`, plus `__str__`, `update`, and
  `to_dictionary`.

## Running the tests
## Author

Chouu - ALU Higher Level Programming
