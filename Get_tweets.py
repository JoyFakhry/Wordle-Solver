import tweepy

bearer = 'AAAAAAAAAAAAAAAAAAAAAHUTiAEAAAAAAqj7tF1GKknkMYlUBq9du92ipRY%3DFOfsnU1jmVK0Ru8jVQBP7VGFBKX1jjztwd9IpOpgGNp9CcSNh9'
client = tweepy.Client(bearer_token=bearer)
id = '1479469664623378433' #WordleStats

tweets = client.get_users_tweets(id=id, max_results=5)

def process_data(how_recent = 0):
   most_recent = tweets.data[how_recent].text
   most_recent = most_recent.split("\n")
   print(most_recent[0])
   data = most_recent[4:11]
   scores = []
   for score in data:
      scores.append(int(score[-3:-1]))
   print(*scores, sep=", ")
   print()

process_data(0)
process_data(1)
