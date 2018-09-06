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
    check50.run("./crack 50.jPgLzVirkc").stdout("hi", timeout=20).exit(0)

@check50.check(compiles)
def cracks_jason():
    """cracks jason's password: 50YHuxoCN9Jkc"""
    check50.run("./crack 50YHuxoCN9Jkc").stdout("JH", timeout=20).exit(0)

@check50.check(compiles)
def cracks_malan():
    """cracks malan's password: 50QvlJWn2qJGE"""
    check50.run("./crack 50QvlJWn2qJGE").stdout("NOPE", timeout=20).exit(0)

@check50.check(compiles)
def cracks_mzlatkova():
    """cracks mzlatkova's password: 50CPlMDLT06yY"""
    check50.run("./crack 50CPlMDLT06yY").stdout("ha", timeout=20).exit(0)

@check50.check(compiles)
def cracks_patrick():
    """cracks patrick's password: 50WUNAFdX/yjA"""
    check50.run("./crack 50WUNAFdX/yjA").stdout("Yale", timeout=20).exit(0)

@check50.check(compiles)
def cracks_rbowden():
    """cracks rbowden's password: 50fkUxYHbnXGw"""
    check50.run("./crack 50fkUxYHbnXGw").stdout("rofl", timeout=20).exit(0)

@check50.check(compiles)
def cracks_summer():
    """cracks summer's password: 50C6B0oz0HWzo"""
    check50.run("./crack 50C6B0oz0HWzo").stdout("FTW", timeout=20).exit(0)

@check50.check(compiles)
def cracks_stelios():
    """cracks stelios's password: 50nq4RV/NVU0I"""
    check50.run("./crack 50nq4RV/NVU0I").stdout("ABC", timeout=20).exit(0)

@check50.check(compiles)
def cracks_wmartin():
    """cracks wmartin's password: 50vtwu4ujL.Dk"""
    check50.run("./crack 50vtwu4ujL.Dk").stdout("haha", timeout=20).exit(0)

@check50.check(compiles)
def cracks_zamyla():
    """cracks zamyla's password: 50i2t3sOSAZtk"""
    check50.run("./crack 50i2t3sOSAZtk").stdout("lol", timeout=20).exit(0)
