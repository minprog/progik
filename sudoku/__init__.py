import check50
import uva.check50.py
import check50.internal
import re
import os
import sys
import itertools

check50.internal.register.before_every(lambda : sys.path.append(os.getcwd()))
check50.internal.register.after_every(lambda : sys.path.pop())

@check50.check()
def exists():
    """sudoku.ipynb exists."""
    check50.include("easy", "hard")
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
    with uva.check50.py.capture_stdout() as out:
        module.show(sudoku)

    expected = ["7 9 _   _ _ _   3 _ 1",
                "_ _ _   _ _ 6   9 _ _",
                "8 _ _   _ 3 _   _ 7 6",
                "",
                "_ _ _   _ _ 5   _ _ 2",
                "_ _ 5   4 1 8   7 _ _",
                "4 _ _   7 _ _   _ _ _",
                "",
                "6 1 _   _ 9 _   _ _ 8",
                "_ _ 2   3 _ _   _ _ _",
                "_ _ 9   _ _ _   _ 5 4"]

    actual = [line.strip() for line in out.getvalue().split("\n")]

    for actual_line, expected_line in zip(actual, expected):
        if actual_line != expected_line:
            raise check50.Mismatch(expected_line, actual_line)


@check50.check(compiles)
def correct_candidates_1_1():
    """candidates() returns 2,3,4,5 for puzzle1 at 1,1"""
    module = uva.check50.py.run("sudoku.py").module
    sudoku = module.load("easy/puzzle1.sudoku")

    expected = {2,3,4,5}
    actual = module.candidates(sudoku, 1, 1)

    try:
        set(actual)
    except TypeError:
        raise check50.Failure(f"expected candidates() to return a set not a {type(actual)}")

    if set(actual) != expected:
        raise check50.Mismatch(actual, expected)


@check50.check(correct_show, timeout=20)
def correct_solve_rule():
    """solve_rule() can solve puzzle1"""
    module = uva.check50.py.run("sudoku.py").module
    sudoku = module.load("easy/puzzle1.sudoku")

    actual = module.solve_rule(sudoku)

    if not isinstance(actual, list):
        actual = sudoku

    check_solved(actual)


@check50.check(correct_show, timeout=20)
def correct_solve_dfs_it():
    """solve_dfs_it() can solve puzzle4"""
    module = uva.check50.py.run("sudoku.py").module
    sudoku = module.load("hard/puzzle4.sudoku")

    actual = module.solve_dfs_it(sudoku)

    if not isinstance(actual, list):
        actual = sudoku

    check_solved(actual)


@check50.check(correct_show, timeout=20)
def correct_solve_dfs_rec():
    """solve_dfs_rec() can solve puzzle4"""
    module = uva.check50.py.run("sudoku.py").module
    sudoku = module.load("hard/puzzle4.sudoku")

    actual = module.solve_dfs_rec(sudoku)

    if not isinstance(actual, list):
        actual = sudoku

    check_solved(actual)


def check_solved(sudoku):
    expected = set(range(1, 10))
    for i in range(9):
        row = sudoku[i]
        column = [sudoku[x][i] for x in range(9)]
        grid = [sudoku[x][y] for x, y in itertools.product([j + (i % 3 * 3) for j in range(3)],
                                                           [j + (i // 3 * 3) for j in range(3)])]
        if set(row) != expected:
            raise check50.Failure(f"This row {row} at x={i} does not contain the numbers 1 to 9")

        if set(column) != expected:
            raise check50.Failure(f"This column {column} at y={i} does not contain the numbers 1 to 9")

        if set(grid) != expected:
            raise check50.Failure(f"This grid {grid} at x={i % 3 * 3}..{i % 3 * 3 + 2}, and y={i // 3 * 3}..{i // 3 * 3 + 2} does not contain the numbers 1 to 9")
