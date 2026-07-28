#!/usr/bin/python3
"""Module that defines a Student class with reload_from_json."""


class Student:
    """Defines a student by first_name, last_name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance,
        optionally filtered by attrs."""
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
