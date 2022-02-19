import argparse
import tweets

from tweets import Tweet

def main(term):
    """This has sample content"""
    print(f"The term is: {term}")
    

def counttweets(filename):
    """Count all the unique tweets in a file."""
    co=0
    with open(filename) as file:
        for line in file:
            co+=1
    return co    





def searchterms(filename,terms=None):
    """Search the file for a list of terms"""
    if type(terms) != list:
        terms=list(terms)
    tweets=[]
    with open(filename) as file:
        for line in file:
            tweet = Tweet(line)
            if terms[0] in tweet:
                tweets.append(tweet)
    return tweets





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--term", type=str, required=True, help="The term to look up in the tweets"
    )
    args = parser.parse_args()
    print(args)
    main(args.term)
    # print("Usage: tweetercounter.py burritos")
