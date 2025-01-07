# Libraries
import re
import os
import nltk
import joblib
import requests
import numpy as np
from bs4 import BeautifulSoup
import urllib.request as urllib
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS
from flask import Flask, render_template, request
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



# Function to fetech youtube comments with chromedriver
def returnytcomments(url):
    data = []  # List to store the comments
    chrome_service = Service(r'C:/chromedriver.exe')

    # Initialize the Chrome driver
    with Chrome(service=chrome_service) as driver:
        # Wait for elements to load (maximum wait time: 15 seconds)
        wait = WebDriverWait(driver, 15)
        # driver.get("https://www.google.com")
        # print("Chrome is working")
        # Open the YouTube video URL
        driver.get(url)

        # Scroll down to load comments multiple times (5 scrolls in this case)
        for item in range(5): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(2)  # Pause to let comments load

        # Extract all comments with the specified CSS selector
        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
            data.append(comment.text)

    return data

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def returnsentiment(text):
    # Get the sentiment score
    score = sia.polarity_scores(text)['compound']

    # Determine sentiment based on score
    if score > 0:
        sentiment = 'Positive'
    elif score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return score, sentiment

# Example comments
cleaned_comments = [
    "video amazing loved",
    "worst video ever total waste time",
    "think editing could better okay",
    "great content keep"
]

# Analyze sentiment
for comment in cleaned_comments:
    score, sentiment = returnsentiment(comment)
    print(f"Comment: {comment}")
    print(f"Sentiment: {sentiment}, Score: {score}")
    print("-" * 30)

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os

class CleanCache:
    '''
    This class is responsible for clearing residual image files from past searches.
    '''
    def __init__(self, directory=None):
        self.clean_path = directory
        if os.listdir(self.clean_path):  # Proceed only if the directory is not empty
            files = os.listdir(self.clean_path)
            for file_name in files:
                os.remove(os.path.join(self.clean_path, file_name))
        print("Cache cleaned!")

def create_wordcloud(cleaned_comments):
    # Combine all cleaned comments into a single string
    combined_text = ' '.join(cleaned_comments)

    # Define stopwords (optional additional stopwords can be added here)
    wc_stopwords = set(STOPWORDS)

    # Generate the Word Cloud
    wordcloud = WordCloud(
        width=1400,
        height=800,
        stopwords=wc_stopwords,
        background_color='white'
    ).generate(combined_text)

    # Display the Word Cloud
    plt.figure(figsize=(14, 8), facecolor='k')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()

    # Clear the cache directory
    CleanCache(directory='static/images')

    # Save the Word Cloud image
    plt.savefig('static/images/woc.png')
    plt.close()
    
# Example cleaned comments
cleaned_comments = [
    "video amazing loved",
    "worst video ever total waste time",
    "think editing could better okay",
    "great content keep"
]

# Generate Word Cloud
create_wordcloud(cleaned_comments)

print("Word Cloud generated and saved in static/images/woc.png.")

