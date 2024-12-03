import nltk
from textblob import TextBlob
import matplotlib.pyplot as plt

# Download NLTK resources (only need to run once)
nltk.download('vader_lexicon')

# Function to analyze sentiment of tweets
def analyze_sentiment(tweet):
    # Create a TextBlob object
    blob = TextBlob(tweet)
    
    # Get the sentiment polarity (ranges from -1 to 1)
    sentiment = blob.sentiment.polarity
    return sentiment

# Read tweets from file
tweets = []
with open('tweets.txt', 'r') as file:
    tweets = file.readlines()

# Analyze sentiment of each tweet
sentiments = [analyze_sentiment(tweet) for tweet in tweets]

# Plot the results
plt.hist(sentiments, bins=20, color='blue', edgecolor='black')
plt.title('Sentiment Analysis of Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.savefig('sentiment_chart.png')  # Save the chart as a PNG file
plt.show()
import nltk
from textblob import TextBlob
import matplotlib.pyplot as plt

# Download NLTK resources (only need to run once)
nltk.download('vader_lexicon')

# Function to analyze sentiment of tweets
def analyze_sentiment(tweet):
    # Create a TextBlob object
    blob = TextBlob(tweet)
    
    # Get the sentiment polarity (ranges from -1 to 1)
    sentiment = blob.sentiment.polarity
    return sentiment

# Read tweets from file
tweets = []
with open('tweets.txt', 'r') as file:
    tweets = file.readlines()

# Analyze sentiment of each tweet
sentiments = [analyze_sentiment(tweet) for tweet in tweets]

# Plot the results
plt.hist(sentiments, bins=20, color='blue', edgecolor='black')
plt.title('Sentiment Analysis of Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.savefig('sentiment_chart.png')  # Save the chart as a PNG file
plt.show()
