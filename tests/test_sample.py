from textblob import TextBlob

def test_sentiment():
    text = "I love this project"
    sentiment = TextBlob(text).sentiment.polarity
    assert sentiment > 0