from ..checkings import Typed, Sized
from . import export

@export
class Set(Typed):
    expected_type = set

@export
class SizedSet(Set, Sized):
    pass

@export
class StringSet(Set):
    secondary_type = str

@export
class SizedStringSet(StringSet, Sized):
    pass

@export
class IntegerSet(Set):
    secondary_type = int

@export
class SizedIntegerSet(IntegerSet, Sized):
    pass

@export
class FloatSet(Set):
    secondary_type = float

@export
class SizedFloatSet(FloatSet, Sized):
    pass

@export
class BoolSet(Set):
    secondary_type = bool

@export
class SizedBoolSet(BoolSet, Sized):
    pass

@export
class ComplexSet(Set):
    secondary_type = complex

@export
class SizedComplexSet(ComplexSet, Sized):
    pass