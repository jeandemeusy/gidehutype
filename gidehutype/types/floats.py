from ..checkings import (Negative, Positive, Restricted, StrictNegative,
                         StrictPositive, Typed)
from . import export


@export
class Float(Typed):
    expected_type = float

@export
class PositiveFloat(Float, Positive):
    pass

@export
class StrictPositiveFloat(Float, StrictPositive):
    pass

@export
class NegativeFloat(Float, Negative):
    pass

@export
class StrictNegativeFloat(Float, StrictNegative):
    pass

@export
class RestrictedFloat(Float, Restricted):
    pass