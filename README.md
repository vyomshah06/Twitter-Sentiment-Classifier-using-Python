# Twitter-Sentiment-Classifier-using-Python
This Project is a part of the Python 3 Programming Specialization course offered by University of Michigan in Coursera. Here, with a little customization, the data is not fake and rendering real time data of twitter through API using Tweepy. Note: No use of NLP algorithms, purely based on python.

## About
The real time twitter data is obtained from Twitter API and stored in a csv file named "project_twitter_data.csv" which has only the text of the tweet. For using the twitter API, it needs API keys and access tokens which are stored in "auth.json" file and one can place their own secret keys in this file. We have also words that express positive sentiment and negative sentiment, in the files "positive_words.txt" and "negative_words.txt".

The task is to build a sentiment classifier, which will detect how positive or negative each tweet is. We will create a csv file named "resulting_data.csv", which contains columns for the Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet.

## Workflow
1. Get API keys from twitter developer account.

2. Store them in a file named "auth.json"(replace XXXX with your API keys).

3. Function to get the twitter data through API written in "twitter_data.py".

4. Classifier code written in "sentiment_classifier.py".

5. Simply run "sentiment_classifier.py" file from your python setup path to generate "project_twitter_data.csv" and "resulting_data.csv"

## Functions

#### 1. def get_tweets(query, cnt = 20): 

It takes the query and count parameters to generate the twitter data based on the text passed in query and number of tweets based on count. This function generates the tweet_text and stores it in "project_twitter_data.csv" file.

#### 2. def strip_punctuation(word):

This function strips all the punctuations which are not needed for sentiment classifier in the text of the tweets. It takes one string word and strips the punctuations.

#### 3. def get_pos(text):

It calculates how many words are considered positive in one sentence or a tweet. Use the list, positive_words to determine what words will count as positive. The function returns a positive integer - how many occurances there are of positive words in the text.

#### 4. def get_neg(text):

It calculates how many words are considered negative in one sentence or a tweet. Use the list, negative_words to determine what words will count as negative. The function returns a positive integer - how many occurances there are of negative words in the text.

## Information
Course material: University of Michigan in Coursera. You can find more information at https://www.coursera.org/learn/python-functions-files-dictionaries/
