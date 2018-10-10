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

    pairs = "".join([generateVirus(10) for _ in range(100)])

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

    pairs = "".join([virus.mutate(virus.generateVirus(10)) for _ in range(100)])

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


@check50.check(generate_virus_elements)
def kill_no_modify():
    """kill() does not modify the list of viruses it accepts as argument"""
    virus = uva.check50.py.run("virus.py").module

    if not isinstance(virus.kill(["AAAA"], 0.25), list):
        raise check50.Failure("expected kill() to return a list")

    viruses = [virus.generateVirus(4) for i in range(10)]
    viruses_copy = viruses[:]
    new_viruses = virus.kill(viruses, 1)

    if viruses != viruses_copy:
        raise check50.Failure(f"the viruses passed in changed from {viruses_copy} to {viruses}")


@check50.check(kill_no_modify)
def kill_no_new():
    """kill() does not produce any new viruses"""
    virus = uva.check50.py.run("virus.py").module

    viruses = [virus.generateVirus(4) for i in range(100)]
    new_viruses = virus.kill(viruses, 0.25)

    if set(new_viruses).difference(set(viruses)) or len(new_viruses) > len(viruses):
        raise check50.Failure("expected no new viruses")


@check50.check(kill_no_modify)
def kill_enough():
    """kill() kills enough viruses according to mortality probability"""
    virus = uva.check50.py.run("virus.py").module

    viruses = [virus.generateVirus(4) for i in range(100)]

    avg_pop_size = sum(len(virus.kill(viruses[:], 0.25)) for i in range(1000)) / 1000

    if not 70 <= avg_pop_size <= 80:
        raise check50.Failure(f"expected roughly 25% of the population to die with mortalityProb of 0.25, but {100 - avg_pop_size}% died!")


@check50.check(generate_virus_elements)
def reproduce_parents():
    """reproduce() with reproductionRate = 0 produces no new viruses"""
    virus = uva.check50.py.run("virus.py").module

    viruses = [virus.generateVirus(4) for i in range(100)]
    new_viruses = virus.reproduce(viruses, 0.25, 0)

    if not isinstance(new_viruses, list):
        raise check50.Failure("expected reproduce() to return a list")

    if not new_viruses == viruses:
        if len(new_viruses) < len(viruses):
            raise check50.Failure("did not expect fewer viruses after reproduce()")
        elif len(new_viruses) > len(viruses):
            raise check50.Failure(f"expected no new viruses")
        else:
            raise check50.Failure("did not expect to find different viruses")


@check50.check(reproduce_parents)
def reproduce_avg():
    """reproduce() produces enough viruses on avg according to reproductionRate"""
    virus = uva.check50.py.run("virus.py").module

    viruses = [virus.generateVirus(4) for i in range(100)]
    new_viruses = virus.reproduce(viruses, 0.25, 0)

    n_trials = 1000
    avg_pop_size = sum(len(virus.reproduce(viruses[:], 0.25, 0.50)) for _ in range(n_trials)) / n_trials

    if not 145 <= avg_pop_size <= 155:
        raise check50.Failure(f"expected roughly a 50% increase in population with a reproductionRate of .5, not {avg_pop_size - 100}%")


@check50.check(reproduce_avg)
def simulate_length():
    """simulate() produces a list of the correct length"""
    virus = uva.check50.py.run("virus.py").module

    viruses = [virus.generateVirus(4) for i in range(100)]
    sim_results = virus.simulate(viruses, 0, 0, 0, 100, 500)

    if not isinstance(sim_results, list):
        raise check50.Failure("expected simulate() to return a list")

    if not len(sim_results) == 501:
        raise check50.Failure(f"expected a list of 501 long with timesteps=500, but found a list {len(sim_results)} long")


@check50.check(simulate_length)
def simulate_fluctuations():
    """simulate(viruses, 0, 0, 0, 100) shows no fluctuations in population size"""
    virus = uva.check50.py.run("virus.py").module

    viruses = [virus.generateVirus(4) for i in range(100)]

    for pop_size in virus.simulate(viruses, 0, 0, 0, 100, 500):
        if pop_size != 100:
            raise check50.Failure(f"expected 100 viruses, but found {pop_size}")


@check50.check(simulate_fluctuations, timeout=30)
def simulate_avg():
    """simulate(viruses, 0.25, 0.1, 0.5, 100)) is correct"""
    virus = uva.check50.py.run("virus.py").module

    viruses = [virus.generateVirus(4) for i in range(100)]

    n_trials = 100
    timesteps = 1000

    avg = lambda : sum(virus.simulate(viruses[:], 0.25, 0.1, 0.5, 100, timesteps)) / timesteps
    avg_pop_size = sum(avg() for _ in range(n_trials)) / n_trials

    if not 40 <= avg_pop_size <= 45:
        raise check50.Failure("expected an average population size between of roughly 40 to 45, but found {avg_pop_size}")


@check50.check(compiles)
def is_resistent_AAA():
    """isResistent(\"AAA\") produces True"""
    isResistent = uva.check50.py.run("virus.py").module.isResistent
    result = isResistent("AAA")

    if result != True:
        raise check50.Failure(f"expected True but found {result}")


@check50.check(compiles)
def is_resistent_AAGGAA():
    """isResistent(\"AAGGAA\") produces False"""
    isResistent = uva.check50.py.run("virus.py").module.isResistent
    result = isResistent("AAGGAA")

    if result != False:
        raise check50.Failure(f"expected False but found {result}")


@check50.check(compiles)
def is_resistent_ATGCAATGCAATGGGCCCCTTTAAACCCT(test):
    """"isResistent(\"ATGCAATGCAATGGGCCCCTTTAAACCCT\") produces True"""
    isResistent = uva.check50.py.run("virus.py").module.isResistent
    result = isResistent("ATGCAATGCAATGGGCCCCTTTAAACCCT")

    if result != True:
        raise check50.Failure(f"expected True but found {result}")
