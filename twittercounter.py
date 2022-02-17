import argparse

def main(term):
	"""This has sample content """
	print(f"The term is: {term}")
	pass

if __name__=="__main__":
	parser= argparse.ArgumentParser()
	parser.add_argument("--term", type=str,required=True,help="The term to look up in the tweets")
	args =parser.parse_args()
	print(args)
	main(args.term)
	#print("Usage: tweetercounter.py burritos")
