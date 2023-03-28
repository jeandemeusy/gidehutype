from ..checkings import Typed, Sized
from . import export

@export
class List(Typed):
    expected_type = list

@export
class IntegerList(List):
    secondary_type = int

@export
class FloatList(List):
    secondary_type = float

@export
class StringList(List):
    secondary_type = str

@export
class BoolList(List):
    secondary_type = bool

@export
class ComplexList(List):
    secondary_type = complex 

@export
class SizedList(List, Sized):
    pass

@export
class SizedIntegerList(IntegerList, Sized):
    pass

@export
class SizedFloatList(FloatList, Sized):
    pass

@export
class SizedStringList(StringList, Sized):
    pass

@export
class SizedBoolList(BoolList, Sized):
    pass

@export
class SizedComplexList(ComplexList, Sized):
    pass