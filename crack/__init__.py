import check50
import check50.c

@check50.check()
def exists():
    """crack.c exists."""
    check50.exists("crack.c")

@check50.check(exists)
def compiles():
    """crack.c compiles."""
    check50.c.compile("crack.c", lcs50=True, lcrypt=True)

@check50.check(compiles)
def cracks_andi():
    """cracks andi's password: 50.jPgLzVirkc"""
    check50.run("./crack 50.jPgLzVirkc").stdout("hi").exit(0)
