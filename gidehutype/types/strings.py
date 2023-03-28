from ..checkings import Typed, Sized, Regex
from . import export

@export
class String(Typed):
    expected_type = str

@export
class SizedString(String, Sized):
    pass

@export
class RegexString(String, Regex):
    pass

@export
class SizedRegexString(String, Sized, Regex):
    pass