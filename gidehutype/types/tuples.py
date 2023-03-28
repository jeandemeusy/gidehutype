from ..checkings import Sized, Typed
from . import export


@export
class Tuple(Typed):
    expected_type = tuple

@export
class IntegerTuple(Tuple):
    secondary_type = int

@export
class FloatTuple(Tuple):
    secondary_type = float

@export
class StringTuple(Tuple):
    secondary_type = str

@export
class BoolTuple(Tuple):
    secondary_type = bool

@export
class ComplexTuple(Tuple):
    secondary_type = complex

@export
class SizedTuple(Tuple, Sized):
    pass

@export
class SizedIntegerTuple(IntegerTuple, Sized):
    pass

@export
class SizedFloatTuple(FloatTuple, Sized):
    pass

@export
class SizedStringTuple(StringTuple, Sized):
    pass

@export
class SizedBoolTuple(BoolTuple, Sized):
    pass

@export
class SizedComplexTuple(ComplexTuple, Sized):
    pass