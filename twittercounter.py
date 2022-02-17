import argparse


def main(term):
    """This has sample content"""
    print(f"The term is: {term}")
    

def counttweets(filename):
	"""Count all the unique tweets in a file."""
	return -1

def searchterms(filename,terms=None)
	"""Search the file for a list of terms."""
	return list()





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--term", type=str, required=True, help="The term to look up in the tweets"
    )
    args = parser.parse_args()
    print(args)
    main(args.term)
    # print("Usage: tweetercounter.py burritos")
