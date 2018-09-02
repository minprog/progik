import check50
import check50.c

@check50.check()
def exists():
    """water.c exists."""
    check50.exists("water.c")

@check50.check(exists)
def compiles():
    """water.c compiles."""
    check50.c.compile("water.c", lcs50=True)

@check50.check(compiles)
def test1():
    """1 minute equals 12 bottles."""
    check50.run("./water").stdin("1").stdout(bottles(12), "12\n").exit(0)

@check50.check(compiles)
def test2():
    """2 minute equals 24 bottles."""
    check50.run("./water").stdin("2").stdout(bottles(24), "24\n").exit(0)

@check50.check(compiles)
def test5(self):
    """5 minute equals 60 bottles."""
    check50.run("./water").stdin("5").stdout(bottles(60), "60\n").exit(0)

@check50.check(compiles)
def test10(self):
    """10 minute equals 120 bottles."""
    check50.run("./water").stdin("10").stdout(bottles(120), "120\n").exit(0)

@check50.check(compiles)
def test_reject_foo(self):
    """rejects "foo" minutes"""
    check50.run("./water").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty(self):
    """rejects "" minutes"""
    check50.run("./water").stdin("").reject()

@check50.check(compiles)
def test_reject_123abc(self):
    """rejects "123abc" minutes"""
    check50.run("./water").stdin("123abc").reject()


def bottles(num):
    return "(^|[^\d]){}[^\d]".format(num)
