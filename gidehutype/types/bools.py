from ..checkings import Typed
from . import export


@export
class Bool(Typed):
    expected_type = bool