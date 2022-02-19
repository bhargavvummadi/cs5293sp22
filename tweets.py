import json
import logging


class Tweet:
    def __init__(self, tweetstring):
        self._tweetstring = tweetstring

    @property
    def text(self):
        """Returns the text of the tweet"""
        return json.loads(self._tweetstring)["text"]

    def id(self):
        return json.loads(self._tweetstring)["_id"]

    def __contains__(self, term):
        logging.debug(f"{term}->[[[{self.text}]]]")
        return term in self.text

    def __str__(self):
        return f"<{self.id()}: {self.text[:50]} >"

    def __repr__(self):
        return f"<{self.id()}>"


if __name__ == "__main__":
    with open("resources/tweets.json") as tweetfile:
        tweetstring = tweetfile.readline()
        tweet = Tweet(tweetstring)
        print(tweet)
        print(tweet.text)
