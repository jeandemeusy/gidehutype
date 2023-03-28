from ..checkings import Typed
from . import export


@export
class Complex(Typed):
    expected_type = complex