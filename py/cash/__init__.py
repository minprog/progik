import check50
import uva.check50.py
import re

@check50.check()
def exists():
    """cash.py exists"""
    check50.exists("cash.py")


@check50.check(exists)
def compiles():
    """cash.py compiles"""
    uva.check50.py.compile("cash.py")


@check50.check(compiles)
def test041():
    """input of 0.41 yields output of 4"""
    result = uva.check50.py.run("cash.py", stdin=["0.41"])
    if not coins(4).match(result.stdout):
        raise check50.Mismatch("4\n", result.stdout)


@check50.check(compiles)
def test001():
    """input of 0.01 yields output of 1"""
    result = uva.check50.py.run("cash.py", stdin=["0.01"])
    if not coins(1).match(result.stdout):
        raise check50.Mismatch("1\n", result.stdout)


@check50.check(compiles)
def test015():
    """input of 0.15 yields output of 2"""
    result = uva.check50.py.run("cash.py", stdin=["0.15"])
    if not coins(2).match(result.stdout):
        raise check50.Mismatch("2\n", result.stdout)


@check50.check(compiles)
def test160():
    """input of 1.6 yields output of 7"""
    result = uva.check50.py.run("cash.py", stdin=["1.6"])
    if not coins(7).match(result.stdout):
        raise check50.Mismatch("7\n", result.stdout)


@check50.check(compiles)
def test230():
    """input of 23 yields output of 92"""
    result = uva.check50.py.run("cash.py", stdin=["23"])
    if not coins(92).match(result.stdout):
        raise check50.Mismatch("92\n", result.stdout)


@check50.check(compiles)
def test420():
    """input of 4.2 yields output of 18"""
    result = uva.check50.py.run("cash.py", stdin=["4.2"])
    if not coins(18).match(result.stdout):
        help = None
        if coins(22).match(result.stdout):
            help = "did you forget to round your input to the nearest cent?"
        raise check50.Mismatch("18\n", actual, help=help)


@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    result = uva.check50.py.run("cash.py", stdin=["-1", "2"])
    if result.stdin:
        raise check50.Failure("expected stdin to be empty!")


def coins(num):
    # regex that matches `num` not surrounded by any other numbers (so coins(2) won't match e.g. 123)
    return re.compile(fr".*(?<![\d]){num}(?![\d]).*", re.MULTILINE)
