import check50
import uva.check50.py
import re

@check50.check()
def exists():
    """hello.py exists."""
    check50.exists("hello.py")

@check50.check(exists)
def compiles():
    """hello.py compiles."""
    uva.check50.py.compile("hello.py")

@check50.check(compiles)
def prints_hello():
    """prints "hello, world\\n" """
    from re import match

    expected = "[Hh]ello, world!?\n"

    result = uva.check50.py.run("hello.py")

    if not re.search(expected, result.stdout):
        help = None
        if re.search(expected[:-1], result.stdout):
            help = r"did you forget a newline ('\n') at the end of your printf string?"
        raise check50.Mismatch("hello, world\n", result.stdout, help=help)
