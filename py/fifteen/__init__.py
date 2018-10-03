import check50
import uva.check50.py
import re

@check50.check()
def exists():
    """fifteen.py exists."""
    check50.exists("fifteen.py")


@check50.check(exists)
def compiles():
    """fifteen.py compiles."""
    uva.check50.py.compile("fifteen.py")


@check50.check(compiles)
def init3():
    """initializes a 3x3 board correctly."""
    result = uva.check50.py.run("fifteen.py", argv=["fifteen.py", "3"], stdin=["-1"])

    expected = re.compile(
          "(08 07 06)[ ]*(\n)"
          "(05 04 03)[ ]*(\n)"
          "(02 01 __)[ ]*(\n)", re.MULTILINE)

    if not expected.search(result.stdout):
        raise check50.Mismatch("08 07 06\n05 04 03\n02 01 __\n", result.stdout)


@check50.check(compiles)
def init4():
    """initializes a 4x4 board correctly."""
    result = uva.check50.py.run("fifteen.py", argv=["fifteen.py", "4"], stdin=["-1"])

    expected = re.compile(
          "(15 14 13 12)[ ]*(\n)"
	      "(11 10 09 08)[ ]*(\n)"
	      "(07 06 05 04)[ ]*(\n)"
	      "(03 01 02 __)[ ]*(\n)", re.MULTILINE)

    if not expected.search(result.stdout):
        raise check50.Mismatch("15 14 13 12\n11 10 09 08\n07 06 05 04\n03 02 01 __\n", result.stdout)



@check50.check(init3)
def invalid8():
    """3x3 board: catches moving 8 as an illegal move."""
    result = uva.check50.py.run("fifteen.py", argv=["fifteen.py", "3"], stdin=["8", "-1"])

    expected = re.compile(
          "(08 07 06)[ ]*(\n)"
          "(05 04 03)[ ]*(\n)"
          "(02 01 __)[ ]*(\n)", re.MULTILINE)

    if not expected.search(result.stdout):
        raise check50.Mismatch("08 07 06\n05 04 03\n02 01 __\n", result.stdout)


@check50.check(init3)
def valid1():
    """3x3 board: catches moving 1 as a legal move."""
    result = uva.check50.py.run("fifteen.py", argv=["fifteen.py", "3"], stdin=["1", "-1"])

    expected = re.compile(
          "(08 07 06)[ ]*(\n)"
          "(05 04 03)[ ]*(\n)"
          "(02 __ 01)[ ]*(\n)", re.MULTILINE)

    if not expected.search(result.stdout):
        raise check50.Mismatch("08 07 06\n05 04 03\n02 __ 01\n", result.stdout)


@check50.check(init3)
def move_up2():
    """3x3 board: move blank up twice."""
    result = uva.check50.py.run("fifteen.py", argv=["fifteen.py", "3"], stdin=["3", "6", "-1"])

    expected = re.compile(
          "(08 07 06)[ ]*(\n)"
          "(05 04 __)[ ]*(\n)"
          "(02 01 03)[ ]*(\n)", re.MULTILINE)

    match = expected.search(result.stdout)

    if not match:
        raise check50.Mismatch("08 07 06\n05 04 __\n02 01 03\n", result.stdout)

    stdout = result.stdout[match.end():]

    expected = re.compile(
          "(08 07 __)[ ]*(\n)"
          "(05 04 06)[ ]*(\n)"
          "(02 01 03)[ ]*(\n)", re.MULTILINE)

    if not expected.search(stdout):
        raise check50.Mismatch("08 07 __\n05 04 06\n02 01 03\n", stdout)


@check50.check(init3)
def move_left2():
    """3x3 board: move blank left twice."""
    result = uva.check50.py.run("fifteen.py", argv=["fifteen.py", "3"], stdin=["1", "2", "-1"])

    expected = re.compile(
          "(08 07 06)[ ]*(\n)"
          "(05 04 03)[ ]*(\n)"
          "(02 __ 01)[ ]*(\n)", re.MULTILINE)

    match = expected.search(result.stdout)

    if not match:
        raise check50.Mismatch("08 07 06\n05 04 03\n02 __ 01\n", result.stdout)

    stdout = result.stdout[match.end():]

    expected = re.compile(
          "(08 07 06)[ ]*(\n)"
          "(05 04 03)[ ]*(\n)"
          "(__ 02 01)[ ]*(\n)", re.MULTILINE)

    if not expected.search(stdout):
        raise check50.Mismatch("08 07 06\n05 04 03\n__ 02 01\n", stdout)


check50.check(init3)
def move_left_right():
    """3x3 board: move blank left then right."""
    result = uva.check50.py.run("fifteen.py", argv=["fifteen.py", "3"], stdin=["1", "1", "-1"])

    expected = re.compile(
          "(08 07 06)[ ]*(\n)"
          "(05 04 03)[ ]*(\n)"
          "(02 __ 01)[ ]*(\n)", re.MULTILINE)

    match = expected.search(result.stdout)

    if not match:
        raise check50.Mismatch("08 07 06\n05 04 03\n02 __ 01\n", result.stdout)

    stdout = result.stdout[match.end():]

    expected = re.compile(
          "(08 07 06)[ ]*(\n)"
          "(05 04 03)[ ]*(\n)"
          "(02 01 __)[ ]*(\n)", re.MULTILINE)

    if not expected.search(stdout):
        raise check50.Mismatch("08 07 06\n05 04 03\n02 01 __\n", stdout)


check50.check(init3)
def move_up_down():
    """3x3 board: move blank up then down."""
    result = uva.check50.py.run("fifteen.py", argv=["fifteen.py", "3"], stdin=["3", "3", "-1"])

    expected = re.compile(
          "(08 07 06)[ ]*(\n)"
          "(05 04 __)[ ]*(\n)"
          "(02 01 03)[ ]*(\n)", re.MULTILINE)

    match = expected.search(result.stdout)

    if not match:
        raise check50.Mismatch("08 07 06\n05 04 __\n02 01 03\n", result.stdout)

    stdout = result.stdout[match.end():]

    expected = re.compile(
          "(08 07 06)[ ]*(\n)"
          "(05 04 03)[ ]*(\n)"
          "(02 01 __)[ ]*(\n)", re.MULTILINE)

    if not expected.search(stdout):
        raise check50.Mismatch("08 07 06\n05 04 03\n02 01 __\n", stdout)


@check50.check(init3)
def solve3():
    """solves a 3x3 board."""
    steps = ["3","4","1","2","5","8","7","6",
             "4","1","2","5","8","7","6","4",
             "1","2","4","1","2","3","5","4",
             "7","6","1","2","3","7","4","8",
             "6","4","8","5","7","8","5","6",
             "4","5","6","7","8","6","5","4",
             "7","8"]

    result = uva.check50.py.run("fifteen.py", argv=["fifteen.py", "3"], stdin=steps)

    expected = re.compile(
          "(01 02 03)[ ]*(\n)"
          "(04 05 06)[ ]*(\n)"
          "(07 __ 08)[ ]*(\n)", re.MULTILINE)

    match = expected.search(result.stdout)

    if not match:
        raise check50.Mismatch("01 02 03\n04 05 06\n07 __ 08\n", result.stdout)

    stdout = result.stdout[match.end():]

    expected = re.compile(
          "(01 02 03)[ ]*(\n)"
          "(04 05 06)[ ]*(\n)"
          "(07 08 __)[ ]*(\n)", re.MULTILINE)

    if not expected.search(stdout):
        raise check50.Mismatch("01 02 03\n04 05 06\n07 08 __\n", stdout)


@check50.check(init4)
def solve4():
    """solves a 4x4 board."""
    steps = ["4","5","6","1","2","4","5","6",
             "1","2","3","7","11","10","9","1",
             "2","3","4","5","6","8","1","2",
             "3","4","7","11","10","9","14",
             "13","12","1","2","3","4","14",
             "13","12","1","2","3","4","14",
             "13","12","1","2","3","4","12",
             "9","15","1","2","3","4","12","9",
             "13","14","9","13","14","7","5",
             "9","13","14","15","10","11","5",
             "9","13","7","11","5","9","13",
             "7","11","15","10","5","9","13",
             "15","11","8","6","7","8","14",
             "12","6","7","8","14","12","6",
             "7","8","14","15","11","10","6",
             "7","8","12","15","11","10","15",
             "11","14","12","11","15","10",
             "14","15","11","12"]

    result = uva.check50.py.run("fifteen.py", argv=["fifteen.py", "4"], stdin=steps)

    expected = re.compile(
          "(01 02 03 04)[ ]*(\n)"
	      "(05 06 07 08)[ ]*(\n)"
	      "(09 10 11 __)[ ]*(\n)"
	      "(13 14 15 12)[ ]*(\n)", re.MULTILINE)

    match = expected.search(result.stdout)

    if not match:
        raise check50.Mismatch("01 02 03 04\n05 06 07 08\n09 10 11 __\n13 14 15 12", result.stdout)

    stdout = result.stdout[match.end():]

    expected = re.compile(
          "(01 02 03 04)[ ]*(\n)"
	      "(05 06 07 08)[ ]*(\n)"
	      "(09 10 11 12)[ ]*(\n)"
	      "(13 14 15 __)[ ]*(\n)", re.MULTILINE)

    if not expected.search(stdout):
        raise check50.Mismatch("01 02 03 04\n05 06 07 08\n09 10 11 12\n13 14 15 __", result.stdout)
