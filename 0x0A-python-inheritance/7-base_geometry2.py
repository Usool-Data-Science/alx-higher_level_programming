>>> BaseGeometry = __import__('7-base_geometry').BaseGeometry

>>> bg = BaseGeometry()

>>> bg.integer_validator("my_int", 12)

>>> bg.integer_validator("width", 89)

>>> bg.integer_validator("name", "John")
Traceback (most recent call last):
TypeError: name must be an integer

>>> bg.integer_validator("age", 0)
Traceback (most recent call last):
ValueError: age must be greater than 0

>>> bg.integer_validator("distance", -4)
Traceback (most recent call last):
ValueError: distance must be greater than 0

>>> bg.integer_validator("name", 4.7)
Traceback (most recent call last):
TypeError: name must be an integer

>>> bg.integer_validator("name", )
Traceback (most recent call last):
TypeError: BaseGeometry.integer_validator() missing 1 required positional argument: 'value'

>>> bg.integer_validator("name", [])
Traceback (most recent call last):
TypeError: name must be an integer

>>> bg.integer_validator("name", 4, 7)
Traceback (most recent call last):
TypeError: BaseGeometry.integer_validator() takes 3 positional arguments but 4 were given

>>> bg.integer_validator("name", 1e23453)
Traceback (most recent call last):
TypeError: name must be an integer
