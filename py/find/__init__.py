import check50
import uva.check50.py
import re

@check50.check()
def exists():
    """find.py exists."""
    check50.exists("find.py")


@check50.check(exists)
def compiles():
    """find.py compiles."""
    uva.check50.py.compile("find.py")


@check50.check(compiles)
def finds_begin():
    """finds 28 in 28, 29, 30"""
    result = uva.check50.py.run("find.py", argv=["find.py", "28", "28", "29", "30"])
    if "Found the needle" not in result.stdout:
        raise check50.Mismatch("Found the needle\n", result.stdout)



@check50.check(compiles)
def finds_middle():
    """finds 28 in 27, 28, 29"""
    result = uva.check50.py.run("find.py", argv=["find.py", "28", "27", "28", "29"])
    if "Found the needle" not in result.stdout:
        raise check50.Mismatch("Found the needle\n", result.stdout)


@check50.check(compiles)
def finds_end():
    """finds 28 in 26, 27, 28"""
    result = uva.check50.py.run("find.py", argv=["find.py", "28", "26", "27", "28"])
    if "Found the needle" not in result.stdout:
        raise check50.Mismatch("Found the needle\n", result.stdout)


@check50.check(compiles)
def finds_left_middle():
    """finds 28 in 27, 28, 29, 30"""
    result = uva.check50.py.run("find.py", argv=["find.py", "28", "27", "28", "29", "30"])
    if "Found the needle" not in result.stdout:
        raise check50.Mismatch("Found the needle\n", result.stdout)


@check50.check(compiles)
def finds_right_middle():
    """finds 28 in 26, 27, 28, 29"""
    result = uva.check50.py.run("find.py", argv=["find.py", "28", "26", "27", "28", "29"])
    if "Found the needle" not in result.stdout:
        raise check50.Mismatch("Found the needle\n", result.stdout)


@check50.check(compiles)
def find_end_4():
    """finds 28 in 25, 26, 27, 28"""
    result = uva.check50.py.run("find.py", argv=["find.py", "28", "25", "26", "27", "28"])
    if "Found the needle" not in result.stdout:
        raise check50.Mismatch("Found the needle\n", result.stdout)


@check50.check(compiles)
def not_find_3():
    """doesn't find 28 in 25, 26, 27"""
    result = uva.check50.py.run("find.py", argv=["find.py", "28", "25", "26", "27"])
    if "Did not find the needle" not in result.stdout:
        raise check50.Mismatch("Did not find the needle\n", result.stdout)


@check50.check(compiles)
def not_find_4():
    """doesn't find 28 in 25, 26, 27, 29"""
    result = uva.check50.py.run("find.py", argv=["find.py", "28", "25", "26", "27", "29"])
    if "Did not find the needle" not in result.stdout:
        raise check50.Mismatch("Did not find the needle\n", result.stdout)


@check50.check(compiles)
def finds_random():
    """finds 28 in 30, 27, 28, 26"""
    result = uva.check50.py.run("find.py", argv=["find.py", "28", "30", "27", "28", "26"])
    if "Found the needle" not in result.stdout:
        raise check50.Mismatch("Found the needle\n", result.stdout)


@check50.check(compiles)
def finds_reverse():
    """finds 28 in 30, 29, 28, 27"""
    result = uva.check50.py.run("find.py", argv=["find.py", "28", "30", "29", "28", "27"])
    if "Found the needle" not in result.stdout:
        raise check50.Mismatch("Found the needle\n", result.stdout)


@check50.check(compiles)
def handles_no_args():
    """handles lack of argv[1]"""
    try:
        result = uva.check50.py.run("find.py", argv=["find.py"])
    except uva.check50.py.PythonException as e:
        if not isinstance(e.exception, SystemExit):
            raise e
    else:
        if not "usage: python find.py needle haystack" in result.stdout:
            raise check50.Mismatch("usage: python find.py needle haystack", result.stdout)
