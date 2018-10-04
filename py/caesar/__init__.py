import check50
import uva.check50.py
import re

@check50.check()
def exists():
    """caesar.py exists."""
    check50.exists("caesar.py")


@check50.check(exists)
def compiles():
    """caesar.py compiles."""
    uva.check50.py.compile("caesar.py")


@check50.check(compiles)
def encrypts_a_as_b():
    """encrypts "a" as "b" using 1 as key"""
    result = uva.check50.py.run("caesar.py", argv=["caesar.py", "1"], stdin=["a"])
    if not re.match(".*ciphertext:\s*b\n", result.stdout):
        raise check50.Mismatch("ciphertext: b\n", result.stdout)


@check50.check(compiles)
def encrypts_barfoo_as_yxocll():
    """encrypts "barfoo" as "yxocll" using 23 as key"""
    result = uva.check50.py.run("caesar.py", argv=["caesar.py", "23"], stdin=["barfoo"])
    if not re.match(".*ciphertext:\s*yxocll\n", result.stdout):
        raise check50.Mismatch("ciphertext: yxocll\n", result.stdout)


@check50.check(compiles)
def encrypts_BARFOO_as_EDUIRR():
    """encrypts "BARFOO" as "EDUIRR" using 3 as key"""
    result = uva.check50.py.run("caesar.py", argv=["caesar.py", "3"], stdin=["BARFOO"])
    if not re.match(".*ciphertext:\s*EDUIRR\n", result.stdout):
        raise check50.Mismatch("ciphertext: EDUIRR\n", result.stdout)


@check50.check(compiles)
def encrypts_BaRFoo_FeVJss():
    """encrypts "BaRFoo" as "FeVJss" using 4 as key"""
    result = uva.check50.py.run("caesar.py", argv=["caesar.py", "4"], stdin=["BaRFoo"])
    if not re.match(".*ciphertext:\s*FeVJss\n", result.stdout):
        raise check50.Mismatch("ciphertext: FeVJss\n", result.stdout)


@check50.check(compiles)
def encrypts_barfoo_as_onesbb():
    """encrypts "barfoo" as "onesbb" using 65 as key"""
    result = uva.check50.py.run("caesar.py", argv=["caesar.py", "65"], stdin=["barfoo"])
    if not re.match(".*ciphertext:\s*onesbb\n", result.stdout):
        raise check50.Mismatch("ciphertext: onesbb\n", result.stdout)


@check50.check(compiles)
def checks_for_handling_non_alpha():
    """encrypts "world, say hello!" as "iadxp, emk tqxxa!" using 12 as key"""
    result = uva.check50.py.run("caesar.py", argv=["caesar.py", "12"], stdin=["world, say hello!"])
    if not re.match(".*ciphertext:\s*iadxp, emk tqxxa!\n", result.stdout):
        raise check50.Mismatch("ciphertext: iadxp, emk tqxxa!\n", result.stdout)


@check50.check(compiles)
def handles_no_argv():
    """handles lack of argv[1]"""
    try:
        result = uva.check50.py.run("caesar.py", argv=["caesar.py"])
    except uva.check50.py.PythonException as e:
        if not isinstance(e.exception, SystemExit):
            raise e
    else:
        if not "usage: python caesar.py key" in result.stdout:
            raise check50.Mismatch("usage: python caesar.py key", result.stdout)
