import check50
import uva.check50.py

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

    with uva.check50.py.capture_stdout() as stdout:
        uva.check50.py.import_("hello.py")

    actual = stdout.getvalue()
    if not match(expected, actual):
        help = None
        if match(expected[:-1], actual):
            help = r"did you forget a newline ('\n') at the end of your printf string?"
        raise check50.Mismatch("hello, world\n", actual, help=help)
