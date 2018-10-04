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
    classify = uva.check50.py.run("tweet.py").module.classify

    import helpers
    dates, tweets = helpers.read_tweets("trump.txt")

    positives = helpers.read_words("positive_words.txt")
    negatives = helpers.read_words("negative_words.txt")

    with uva.check50.py.capture_stdout() as stdout:
        classify(tweets, positives, negatives)

    out = stdout.getvalue()

    check_classify(out, "positive", 538)
    return out


@check50.check(correct_positive)
def correct_negative(out):
    """correct number of negative tweets."""
    check_classify(out, "negative", 261)


@check50.check(correct_positive)
def correct_neutral(out):
    """correct number of neutral tweets."""
    check_classify(out, "neutral", 198)


@check50.check(compiles)
def best_words():
    """correct top five positive words."""
    positive_word = uva.check50.py.run("tweet.py").module.positive_word

    import helpers
    dates, tweets = helpers.read_tweets("trump.txt")
    positives = helpers.read_words("positive_words.txt")

    with uva.check50.py.capture_stdout() as stdout:
        positive_word(tweets, positives)

    out = stdout.getvalue()
    top5 = ["great", "trump", "thank", "good", "honor"]

    for word in top5:
        if word not in out:
            raise check50.Mismatch(f"{word}", out)

    for word in set(positives) - set(top5) - {"positive", "top"}:
        if word and word in out:
            raise check50.Failure(f"Did not expect {word} in top 5!")

    return out


@check50.check(best_words)
def occurance_words(out):
    """correct occurance of top five positive words."""
    for word, occ in [("great", 245), ("trump", 88), ("thank", 82), ("good", 55), ("honor", 39)]:
        match = re.search(f"{word}[^\n^\d]*(\d+)", out)
        if not match.groups() or not int(match.groups()[0]) == occ:
            raise check50.Mismatch(f"{word} {occ}", out)


@check50.check(compiles)
def n_days():
    """correct number of bad days."""
    bad_days = uva.check50.py.run("tweet.py").module.bad_days

    import helpers
    dates, tweets = helpers.read_tweets("trump.txt")
    positives = helpers.read_words("positive_words.txt")
    negatives = helpers.read_words("negative_words.txt")

    with uva.check50.py.capture_stdout() as stdout:
        bad_days(dates, tweets, positives, negatives)

    out = stdout.getvalue()

    matches = re.findall("[\d]+[^\n^\d]*[\d]+[^\n^\d]*[\d]+", out)
    if not matches or len(matches) != 31:
        n = len(matches) if matches else 0
        raise check50.Failure(f"expected 31 bad days, but found {n} dates!")

    return out

@check50.check(n_days)
def correct_days(out):
    """correct dates of bad days."""
    days = {(24, 3, 2018), (23, 3, 2018), (21, 3, 2018), (19, 3, 2018),
            (18, 3, 2018), (17, 3, 2018), (13, 3, 2018), (6, 3, 2018),
            (3, 3, 2018), (18, 2, 2018), (17, 2, 2018), (16, 2, 2018),
            (15, 2, 2018), (12, 2, 2018), (10, 2, 2018), (4, 2, 2018),
            (28, 1, 2018), (11, 1, 2018), (7, 1, 2018), (5, 1, 2018),
            (30, 12, 2017), (12, 12, 2017), (11, 12, 2017), (3, 12, 2017),
            (26, 11, 2017), (25, 11, 2017), (20, 11, 2017), (19, 11, 2017),
            (3, 11, 2017), (31, 10, 2017), (30, 10, 2017)}

    days_copy = set(days)

    matches = re.findall("(\d+)[^\n^\d]*(\d+)[^\n^\d]*(\d+)", out)

    for match in matches:
        match = tuple([int(d) for d in match])

        if match in days_copy:
            try:
                days.remove(match)
            except KeyError:
                pass
        else:
            raise check50.Failure(f"Did not expect {match} as a bad day!")

    if days:
        raise check50.Failure(f"Expected to find {days} as bad days.")


def check_classify(out, type, n):
    match = re.search(fr"{type}[^\n^\d]*(\d+)", out)

    if not match or int(match.groups()[0]) != n:
        raise check50.Mismatch(f"{type}: {n}", out)
