from dateutil.parser import parse
import nltk

def read_tweets(tweet_filename):
    """
    read all tweets from tweet_filename
    returns two lists:
        the dates tweets where posted on
        the tweet contents tokenized
    """

    # dates of the tweets
    dates = []
    # contents of the tweets
    tweets = []

    # open and read filename
    with open(tweet_filename, "r") as trump_file:

        # for every line in the file
        for line in trump_file:
            # extract the date from the line
            date = parse(line.split(",")[0])

            # convert date from datetime to string
            date = "{} {} {}".format(date.day, date.month, date.year)

            # extract the tweet content from the line
            tweet_tokens = tokenize(",".join(line.split(",")[1:]))

            # collect the dates and tweet content
            dates.append(date)
            tweets.append(tweet_tokens)

    return dates, tweets

def read_words(filename):
    """
    read all words from filename
    assumes every line contains just one word
    returns a list of words
    """

    # all words in the file
    words = []

    # open filename and read its contents
    with open(filename, "r") as f:
        # for every line in the file
        for line in f:
            # if line does not start with ;
            if not line.startswith(";"):
                # add word on the line to words
                words.append(line.strip())

    return words

def tokenize(tweet):
    """
    tokenize the tweet
    splits the tweet in lowercase words, i.e. tokens
    returns a set of tokens
    """
    tokenizer = nltk.TweetTokenizer()
    return [word.lower() for word in tokenizer.tokenize(tweet)]
