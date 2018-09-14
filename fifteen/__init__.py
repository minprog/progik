import check50
import check50.c

@check50.check()
def exists():
    """fifteen.c exists."""
    check50.exists("fifteen.c")

@check50.check(exists)
def compiles():
    """fifteen.c compiles."""
    # Remove sleeps from student code
    check50.run("sed -i='' '/#include <unistd.h>/a \\\n#define usleep(x)' fifteen.c").exit()

    check50.c.compile("fifteen.c", lcs50=True)

@check50.check(compiles)
def init3():
    """initializes a 3x3 board correctly."""
    board = ["8", "7", "6",
             "5", "4", "3",
             "2", "1", "[_0]"]

    check = check50.run("./fifteen 3")
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")

@check50.check(compiles)
def init4():
    """initializes a 4x4 board correctly."""
    board = ["15", "14", "13", "12",
             "11", "10", "9", "8",
             "7", "6", "5", "4",
             "3", "1", "2", "[_0]"]

    check = check50.run("./fifteen 4")
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")

@check50.check(init3)
def invalid8():
    """3x3 board: catches moving 8 as an illegal move"""
    check = check50.run("./fifteen 3").stdin("8").stdout("Illegal move.")

    board = ["8", "7", "6",
             "5", "4", "3",
             "2", "1", "[_0]"]
    for tile in board:
        check.stdout(tile)
    check.stdout("\n")

# @check("init3")
# def valid1(self):
#     """3x3 board: catches moving 1 as a legal move"""
#     self.spawn("./fifteen 3").stdin("1")                    \
#                              .stdout("8-7-6|5-4-3|2-0-1\n") \
#                              .stdout("Tile to move:")
#
# @check("init3")
# def move_up2(self):
#     """3x3 board: move blank up twice"""
#     self.spawn("./fifteen 3").stdin("3")                    \
#                              .stdout("8-7-6|5-4-0|2-1-3\n") \
#                              .stdin("6")                    \
#                              .stdout("8-7-0|5-4-6|2-1-3\n")
#
# @check("init3")
# def move_left2(self):
#     """3x3 board: move blank left twice"""
#     self.spawn("./fifteen 3").stdin("1")                    \
#                              .stdout("8-7-6|5-4-3|2-0-1\n") \
#                              .stdin("2")                    \
#                              .stdout("8-7-6|5-4-3|0-2-1\n")
#
# @check("init3")
# def move_left_right(self):
#     """3x3 board: move blank left then right"""
#     self.spawn("./fifteen 3").stdin("1")                    \
#                              .stdout("8-7-6|5-4-3|2-0-1\n") \
#                              .stdin("2")                    \
#                              .stdout("8-7-6|5-4-3|2-1-0\n")
#
# @check("init3")
# def move_up_down(self):
#     """3x3 board: move blank up then down"""
#     self.spawn("./fifteen 3").stdin("3")                    \
#                              .stdout("8-7-6|5-4-0|2-1-3\n") \
#                              .stdin("3")                    \
#                              .stdout("8-7-6|5-4-3|2-1-0\n")

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

    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "[_0]"]

    check = check50.run("./fifteen 3")

    for step in steps:
        check.stdin(step, prompt=False)

    for tile in board:
        check.stdout(tile)
    check.stdout("\n")

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

    board = ["1", "2", "3", "4",
             "5", "6", "7", "8",
             "9", "10", "11", "12",
             "13", "14", "15", "[_0]"]

    check = check50.run("./fifteen 4")

    for step in steps:
        check.stdin(step, prompt=False)

    for tile in board:
        check.stdout(tile)
    check.stdout("\n")
