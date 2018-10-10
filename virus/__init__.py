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
    """virus.ipynb exists."""
    check50.exists("virus.ipynb")


@check50.check(exists)
def compiles():
    """virus.ipynb compiles."""
    uva.check50.py.nbconvert("virus.ipynb")

    uva.check50.py.compile("virus.py")
    module = uva.check50.py.run("virus.py").module

    for attr in ["generateVirus", "mutate", "kill",
                 "reproduce", "reproductionProbability", "simulate",
                 "isResistent", "simulateMedicine", "experiment"]:
        if not hasattr(module, attr):
            raise check50.Failure(f"Expected virus.ipynb to have a function called {attr} !")


@check50.check(compiles)
def generate_virus_length():
    """generateVirus() produces viruses of the specified length"""
    generateVirus = uva.check50.py.run("virus.py").module.generateVirus

    if not isinstance(generateVirus(1), str):
        raise check50.Failure("expected generateVirus() to return a str")

    for i in range(10):
        if not len(generateVirus(i)) == i:
            raise check50.Failure(f"expected generateVirus({i}) to produce a virus of length {i}")


@check50.check(generate_virus_length)
def generate_virus_elements():
    """generateVirus() produces viruses consisting only of A, T, G and C"""
    generateVirus = uva.check50.py.run("virus.py").module.generateVirus

    pairs = "".join([generateVirus(10) for _ in range(1000)])

    if any([el not in "AGTC" for el in pairs]):
        raise check50.Failure("expected generateVirus() to return only combinations of AGTC")


@check50.check(generate_virus_elements)
def mutate_length():
    "mutate() produces viruses of the same length as the parent"
    virus = uva.check50.py.run("virus.py").module

    if not isinstance(virus.mutate("AAAA"), str):
        raise check50.Failure("expected mutate() to return a str")

    for i in range(1, 10):
        v = virus.generateVirus(i)
        if not len(v) == len(virus.mutate(v)):
            raise check50.Failure(f"expected mutate() to produce a virus of the same length as the parent")


@check50.check(mutate_length)
def mutate_elements():
    """mutate() produces viruses consisting only of A, T, G and C"""
    virus = uva.check50.py.run("virus.py").module

    pairs = "".join([virus.mutate(virus.generateVirus(10)) for _ in range(1000)])

    if any([el not in "AGTC" for el in pairs]):
        raise check50.Failure("expected mutate() to return only combinations of AGTC")


@check50.check(mutate_length)
def mutate_one_difference():
    """mutate() produces viruses who differ exactly one genome from the parent"""
    virus = uva.check50.py.run("virus.py").module

    off_by_one = lambda col1, col2 : sum(a != b for a, b in zip(col1, col2)) == 1

    for v in [virus.generateVirus(i) for i in range(1, 100)]:
        mutated_v = virus.mutate(v)
        if not off_by_one(mutated_v, v):
            raise check50.Failure(f"expected mutate({v}) to return a virus with only one mutation, not {mutated_v}")
