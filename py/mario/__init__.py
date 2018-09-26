import check50
import check50.uva.py
import re

@check50.check()
def exists():
    """mario.py exists."""
    check50.exists("mario.py")
    check50.include("1.txt", "2.txt", "23.txt")

@check50.check(exists)
def compiles():
    """mario.py compiles."""
    check50.uva.py.compile("mario.py")

@check50.check(compiles)
def test_reject_negative():
    """rejects a height of -1"""
    result = check50.uva.py.run("mario.py", stdin=["-1", "2"])
    if result.stdin:
        raise check50.Failure("Expected stdin to be empty")

@check50.check(compiles)
def test0():
    """handles a height of 0 correctly"""
    result = check50.uva.py.run("mario.py", stdin=["0"])
    if "#" in result.stdout:
        raise check50.Failure("Expected no # in stdout")

@check50.check(compiles)
def test1():
    """handles a height of 1 correctly"""
    result = check50.uva.py.run("mario.py", stdin=["1"])
    check_pyramid(result.stdout, "Height: " + open("1.txt").read())

@check50.check(compiles)
def test2():
    """handles a height of 2 correctly"""
    result = check50.uva.py.run("mario.py", stdin=["2"])
    check_pyramid(result.stdout, "Height: " + open("2.txt").read())

@check50.check(compiles)
def test23():
    """handles a height of 23 correctly"""
    result = check50.uva.py.run("mario.py", stdin=["23"])
    check_pyramid(result.stdout, "Height: " + open("23.txt").read())

@check50.check(compiles)
def test24():
    """rejects a height of 24, and then accepts a height of 2"""
    result = check50.uva.py.run("mario.py", stdin=["24", "2"])
    if result.stdin:
        raise check50.Failure("Expected stdin to be empty")
    check_pyramid(result.stdout, "Height: Height: " + open("2.txt").read())

def check_pyramid(output, correct):
    if output == correct:
        return

    output = output.splitlines()
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)
