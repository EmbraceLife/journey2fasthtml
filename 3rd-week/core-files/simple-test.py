from fastcore.meta import delegates
from fastcore.utils import patch

class A: ...

@patch
def f(self:A): ...