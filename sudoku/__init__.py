import check50
import uva.check50.py
import check50.internal
import os
import sys
import re
import itertools
import copy

check50.internal.register.before_every(lambda : sys.path.append(os.getcwd()))
check50.internal.register.after_every(lambda : sys.path.pop())

@check50.check()
def exists():
    """sudoku.ipynb exists."""
    check50.include("easy", "hard", *[f"puzzle{i}.sudoku" for i in range(1, 7)])
    check50.exists("sudoku.ipynb")


@check50.check(exists)
def compiles():
    """sudoku.py compiles."""
    uva.check50.py.nbconvert("sudoku.ipynb", dest="sudoku.py")
    uva.check50.py.compile("sudoku.py")
    module = uva.check50.py.run("sudoku.py").module

    for attr in ["load", "show", "candidates", "solve_rule", "solve_dfs_it", "solve_dfs_rec"]:
        if not hasattr(module, attr):
            raise check50.Failure(f"Expected tweet.py to have a function called {attr}")


@check50.check(compiles)
def correct_show():
    """show() shows puzzle1 correctly"""
    module = uva.check50.py.run("sudoku.py").module

    sudoku = module.load("easy/puzzle1.sudoku")

    check_sudoku(sudoku)

    with uva.check50.py.capture_stdout() as out:
        module.show(sudoku)

    expected = ["7 9 _  [ ]*_ _ _  [ ]*3 _ 1",
                "_ _ _  [ ]*_ _ 6  [ ]*9 _ _",
                "8 _ _  [ ]*_ 3 _  [ ]*_ 7 6",
                "",
                "_ _ _  [ ]*_ _ 5  [ ]*_ _ 2",
                "_ _ 5  [ ]*4 1 8  [ ]*7 _ _",
                "4 _ _  [ ]*7 _ _  [ ]*_ _ _",
                "",
                "6 1 _  [ ]*_ 9 _  [ ]*_ _ 8",
                "_ _ 2  [ ]*3 _ _  [ ]*_ _ _",
                "_ _ 9  [ ]*_ _ _  [ ]*_ 5 4"]

    actual = [line.strip() for line in out.getvalue().split("\n")]

    for actual_line, expected_line in zip(actual, expected):
        if not re.match(expected_line, actual_line):
            readable_line = expected_line.replace("[", "").replace("]", "").replace("*", "")
            raise check50.Mismatch(readable_line, actual_line)


@check50.check(compiles)
def correct_candidates_1_1():
    """candidates() returns 2,3,4,5 for puzzle1 at 1,1"""
    module = uva.check50.py.run("sudoku.py").module
    sudoku = module.load("easy/puzzle1.sudoku")

    check_sudoku(sudoku)

    expected = {2,3,4,5}
    actual = set([int(c) for c in module.candidates(sudoku, 1, 1)])

    try:
        set(actual)
    except TypeError:
        raise check50.Failure(f"expected candidates() to return a set not a {type(actual)}")

    if set(actual) != expected:
        raise check50.Mismatch(actual, expected)


@check50.check(compiles)
def correct_solve_rule():
    """solve_rule() can solve puzzle1"""
    module = uva.check50.py.run("sudoku.py").module
    sudoku = module.load("easy/puzzle1.sudoku")
    original = copy.deepcopy(sudoku)

    actual = module.solve_rule(sudoku)
    if not isinstance(actual, list):
        actual = sudoku

    check_sudoku(original)
    check_sudoku(actual)
    check_solved(actual, original)


@check50.check(compiles)
def correct_solve_dfs_it():
    """solve_dfs_it() can solve puzzle4"""
    module = uva.check50.py.run("sudoku.py").module
    sudoku = module.load("hard/puzzle4.sudoku")
    original = copy.deepcopy(sudoku)

    actual = module.solve_dfs_it(sudoku)
    if not isinstance(actual, list):
        actual = sudoku

    check_sudoku(original)
    check_sudoku(actual)
    check_solved(actual, original)


@check50.check(compiles)
def correct_solve_dfs_rec():
    """solve_dfs_rec() can solve puzzle4"""
    module = uva.check50.py.run("sudoku.py").module
    sudoku = module.load("hard/puzzle4.sudoku")
    original = copy.deepcopy(sudoku)

    actual = module.solve_dfs_rec(sudoku)
    if not isinstance(actual, list):
        actual = sudoku

    check_sudoku(original)
    check_sudoku(actual)
    check_solved(actual, original)


def check_sudoku(sudoku):
    if len(sudoku) != 9:
        raise check50.Failure(f"Expected the sudoku to be 9 wide, but it's {len(sudoku)} wide")

    for i in range(9):
        if len(sudoku[i]) != 9:
            raise check50.Failure(f"Expected the sudoku to be 9 long, but it's {len(sudoku[i])} long")

    for x, y in itertools.product(range(9), range(9)):
        try:
            int(sudoku[x][y])
        except TypeError:
            raise check50.Failure(f"Expected the sudoku to contain only integers, but found a {type(sudoku[x][y])}")

        if int(sudoku[x][y]) not in set(range(10)):
            raise check50.Failure(f"Expected the sudoku to contain only numbers from 0..9, but found {sudoku[x][y]}")


def check_solved(sudoku, original):
    for x, y in itertools.product(range(9), range(9)):
        if int(original[x][y]) != 0 and sudoku[x][y] != original[x][y]:
            raise check50.Failure(f"The solved sudoku changed from the original sudoku at x={x}, y={y}")

    expected = set(range(1, 10))
    for i in range(9):
        row = [int(v) for v in sudoku[i]]
        column = [int(sudoku[x][i]) for x in range(9)]
        grid = [int(sudoku[x][y]) for x, y in itertools.product([j + (i % 3 * 3) for j in range(3)],
                                                                [j + (i // 3 * 3) for j in range(3)])]
        if set(row) != expected:
            raise check50.Failure(f"This row {row} at x={i} does not contain the numbers 1 to 9")

        if set(column) != expected:
            raise check50.Failure(f"This column {column} at y={i} does not contain the numbers 1 to 9")

        if set(grid) != expected:
            raise check50.Failure(f"This grid {grid} at x={i % 3 * 3}..{i % 3 * 3 + 2}, and y={i // 3 * 3}..{i // 3 * 3 + 2} does not contain the numbers 1 to 9")
