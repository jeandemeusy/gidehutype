from ..checkings import (Negative, Positive, Restricted, StrictNegative,
                         StrictPositive, Typed)
from . import export


@export
class Integer(Typed):
    expected_type = int

@export
class PositiveInteger(Integer, Positive):
    pass

@export
class StrictPositiveInteger(Integer, StrictPositive):
    pass

@export
class NegativeInteger(Integer, Negative):
    pass

@export
class StrictNegativeInteger(Integer, StrictNegative):
    pass

@export
class RestrictedInteger(Integer, Restricted):
    pass