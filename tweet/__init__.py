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
    """tweet.py exists."""
    check50.include("helpers.py", "negative_words.txt", "positive_words.txt", "trump.txt")
    check50.exists("tweet.py")


@check50.check(exists)
def compiles():
    """tweet.py compiles."""
    uva.check50.py.compile("tweet.py")
    module = uva.check50.py.run("tweet.py").module

    for attr in ["classify", "positive_word", "bad_days"]:
        if not hasattr(module, attr):
            raise check50.Failure(f"Expected tweet.py to have a function called {attr} !")


@check50.check(compiles)
def correct_positive():
    """correct number of positive tweets."""
    check_classify("positive", 417)


@check50.check(compiles)
def correct_negative():
    """correct number of negative tweets."""
    check_classify("negative", 130)


@check50.check(compiles)
def correct_neutral():
    """correct number of neutral tweets."""
    check_classify("neutral", 450)


def check_classify(type, n):
    classify = uva.check50.py.run("tweet.py").module.classify

    import helpers
    dates, tweets = helpers.read_tweets("trump.txt")

    positives = helpers.read_words("positive_words.txt")
    negatives = helpers.read_words("negative_words.txt")

    with uva.check50.py.capture_stdout() as stdout:
        classify(tweets, positives, negatives)

    out = stdout.getvalue()
    match = re.search(fr"{type}[ ]*:?[ ]*(\d+)", out)

    if not match or int(match.groups()[0]) != n:
        raise check50.Mismatch(f"{type}: {n}", out)
