import re

from .descriptor import Descriptor


class Typed(Descriptor):
    expected_type = object
    secondary_type = None

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        
        if self.secondary_type:
            try:
                [x for x in value]
            except TypeError:
                raise TypeError(f"Variable not iterable")

            for item in value:
                if not isinstance(item, self.secondary_type):
                    raise TypeError(f"Expected {self.secondary_type} inside iterable")

        super().__set__(instance, value)

class Positive(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            idx_arg = len(instance.__dict__) + 1
            raise ValueError(f"Arg #{idx_arg} must be >= 0")

        super().__set__(instance, value)

class StrictPositive(Descriptor):
    def __set__(self, instance, value):
        if value <= 0:
            idx_arg = len(instance.__dict__) + 1
            raise ValueError(f"Arg #{idx_arg} must be > 0")

        super().__set__(instance, value)

class Negative(Descriptor):
    def __set__(self, instance, value):
        if value > 0:
            idx_arg = len(instance.__dict__) + 1
            raise ValueError(f"Arg #{idx_arg} must be <= 0")

        super().__set__(instance, value)

class StrictNegative(Descriptor):
    def __set__(self, instance, value):
        if value >= 0:
            idx_arg = len(instance.__dict__) + 1
            raise ValueError(f"Arg #{idx_arg} must be < 0")

        super().__set__(instance, value)

class Restricted(Descriptor):
    def __init__(self, *args, minval, maxval, **kwargs):
        self.minval = minval
        self.maxval = maxval
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if value < self.minval or value > self.maxval:
            idx_arg = len(instance.__dict__) + 1
            raise ValueError(f"Arg #{idx_arg} must be between {self.minval} and {self.maxval}")

        super().__set__(instance, value)

class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise ValueError(f"'{value}' must be maximum {self.maxlen} elements long")

        super().__set__(instance, value)

class Regex(Descriptor):
    def __init__(self, *args, pattern, **kwargs):
        self.pattern = re.compile(pattern)
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if not self.pattern.match(value):
            raise ValueError(f"'{value}' must match pattern '{self.pattern.pattern}'")

        super().__set__(instance, value)