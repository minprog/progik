import check50
import check50.uva.py

@check50.check()
def exists():
    """hello.py exists."""
    check50.exists("hello.py")

@check50.check(exists)
def compiles():
    """hello.py compiles."""
    check50.uva.py.compile("hello.py")

@check50.check(compiles)
def prints_hello():
    """prints "hello, world\\n" """
    from re import match

    expected = "[Hh]ello, world!?\n"

    with check50.uva.py.capture_stdout() as stdout:
        check50.uva.py.import_("hello.py")

    actual = stdout.getvalue()
    if not match(expected, actual):
        help = None
        if match(expected[:-1], actual):
            help = r"did you forget a newline ('\n') at the end of your printf string?"
        raise check50.Mismatch("hello, world\n", actual, help=help)
