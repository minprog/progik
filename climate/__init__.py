import check50
import uva.check50.py
import check50.internal
import re
import os
import sys

check50.internal.register.before_every(lambda : sys.path.append(os.getcwd()))
check50.internal.register.after_every(lambda : sys.path.pop())

@check50.check()
def exists():
    """climate.ipynb exists."""
    check50.include("climate.data")
    check50.exists("climate.ipynb")


@check50.check(exists)
def compiles():
    """climate.ipynb compiles."""
    uva.check50.py.nbconvert("climate.ipynb")
    uva.check50.py.compile("climate.py")
    return uva.check50.py.run("climate.py").stdout


@check50.check(compiles)
def correct_max_temp(stdout):
    """prints the maximum temperature measured"""
    match = re.search("De maximale temperatuur was (\d+[\.,]\d+) graden op", stdout)
    if not match:
        raise check50.Mismatch("De maximale temperatuur was XX.XX graden op", stdout)

    answer = float(match.groups(0)[0].replace(",", "."))

    if answer != 36.8:
        raise check50.Failure(f"expected 36.8 but found {answer}")


@check50.check(compiles)
def correct_max_temp_day(stdout):
    """prints the day of the maximum temperature"""
    match = re.search("De maximale temperatuur was \d+[\.,]\d+ graden op (\d+) ([a-zA-Z]{3}) ([\d]{4})", stdout)

    if not match:
        raise check50.Mismatch("De maximale temperatuur was XX.XX graden op XX XXX XXXX", stdout)

    day = int(match.groups()[0])
    month = match.groups()[1]
    year = int(match.groups()[2])

    if day != 27 or month.lower() != "jun" or year != 1947:
        raise check50.Failure(f"expected 27 jun 1947 but found {day} {month} {year}")


@check50.check(compiles)
def correct_min_temp(stdout):
    """prints the minimum temperature measured"""
    match = re.search("De minimale temperatuur was (-\d+[\.,]\d+) graden op", stdout)
    if not match:
        raise check50.Mismatch("De minimale temperatuur was -XX.XX graden op", stdout)

    answer = float(match.groups(0)[0].replace(",", "."))

    if answer != -11.3:
        raise check50.Failure(f"expected -11.3 but found {answer}")


@check50.check(compiles)
def correct_min_temp_day(stdout):
    """prints the day of the minimum temperature"""
    match = re.search("De minimale temperatuur was -\d+[\.,]\d+ graden op (\d+) ([a-zA-Z]{3}) ([\d]{4})", stdout)

    if not match:
        raise check50.Mismatch("De minimale temperatuur was -XX.XX graden op XX XXX XXXX", stdout)

    day = int(match.groups()[0])
    month = match.groups()[1]
    year = int(match.groups()[2])

    if day != 20 or month.lower() != "dec" or year != 1938:
        raise check50.Failure(f"expected 20 dec 1938 but found {day} {month} {year}")
