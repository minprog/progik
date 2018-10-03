import check50
import uva.check50.py
import re

@check50.check()
def exists():
    """vigenere.py exists."""
    check50.exists("vigenere.py")


@check50.check(exists)
def compiles():
    """vigenere.py compiles."""
    uva.check50.py.compile("vigenere.py")


@check50.check(compiles)
def aa():
    """encrypts "a" as "a" using "a" as keyword"""
    result = uva.check50.py.run("vigenere.py", argv=["vigenere.py", "a"], stdin=["a"])
    if not re.match(".*ciphertext:\s*a\n", result.stdout):
        raise check50.Mismatch("ciphertext: a\n", result.stdout)


@check50.check(compiles)
def bazbarfoo_caqgon():
    """encrypts "barfoo" as "caqgon" using "baz" as keyword"""
    result = uva.check50.py.run("vigenere.py", argv=["vigenere.py", "baz"], stdin=["barfoo"])
    if not re.match(".*ciphertext:\s*caqgon\n", result.stdout):
        raise check50.Mismatch("ciphertext: caqgon\n", result.stdout)


@check50.check(compiles)
def mixedBaZBARFOO():
    """encrypts "BaRFoo" as "CaQGon" using "BaZ" as keyword"""
    result = uva.check50.py.run("vigenere.py", argv=["vigenere.py", "BaZ"], stdin=["BaRFoo"])
    if not re.match(".*ciphertext:\s*CaQGon\n", result.stdout):
        raise check50.Mismatch("ciphertext: CaQGon\n", result.stdout)


@check50.check(compiles)
def allcapsBAZBARFOO():
    """encrypts "BARFOO" as "CAQGON" using "BAZ" as keyword"""
    result = uva.check50.py.run("vigenere.py", argv=["vigenere.py", "BAZ"], stdin=["BARFOO"])
    if not re.match(".*ciphertext:\s*CAQGON\n", result.stdout):
        raise check50.Mismatch("ciphertext: CAQGON\n", result.stdout)


@check50.check(compiles)
def bazworld():
    """encrypts "world!$?" as "xoqmd!$?" using "baz" as keyword"""
    result = uva.check50.py.run("vigenere.py", argv=["vigenere.py", "baz"], stdin=["world!$?"])
    if not re.match(".*ciphertext:\s*xoqmd!\$\?\n", result.stdout):
        raise check50.Mismatch("ciphertext: xoqmd!$?\n", result.stdout)


@check50.check(compiles)
def withspaces():
    """encrypts "hello, world!" as "iekmo, vprke!" using "baz" as keyword"""
    result = uva.check50.py.run("vigenere.py", argv=["vigenere.py", "baz"], stdin=["hello, world!"])
    if not re.match(".*ciphertext:\s*iekmo, vprke\!\n", result.stdout):
        raise check50.Mismatch("ciphertext: iekmo, vprke!\n", result.stdout)


@check50.check(compiles)
def noarg():
    """handles lack of argv[1]"""
    try:
        result = uva.check50.py.run("vigenere.py", argv=["vigenere.py"])
    except uva.check50.py.PythonException as e:
        if not isinstance(e.exception, SystemExit):
            raise e
    else:
        if not "usage: python vigenere.py key" in result.stdout:
            raise check50.Mismatch("usage: python vigenere.py key", result.stdout)


@check50.check(compiles)
def toomanyargs():
    """handles argc > 2"""
    try:
        result = uva.check50.py.run("vigenere.py", argv=["vigenere.py", "1", "2", "3"])
    except uva.check50.py.PythonException as e:
        if not isinstance(e.exception, SystemExit):
            raise e
    else:
        if not "usage: python vigenere.py key" in result.stdout:
            raise check50.Mismatch("usage: python vigenere.py key", result.stdout)
