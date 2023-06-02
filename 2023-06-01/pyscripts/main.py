import snscrape.modules.twitter as sntwitter
import pandas as pd

attributes_container = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('groomer until:2019-06-01').get_items()):
	if i>100:
		break
	attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.rawContent])

tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweets"])

tweets_df.to_csv('groomer-2019-06-01.csv', index=False)