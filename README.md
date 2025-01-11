# YouTube Comment Sentiment Analysis Web App

## Short Description
This web application enables users to analyze the sentiment of comments on YouTube videos. By simply providing a YouTube video URL, users can generate insightful sentiment analysis reports, visualize sentiment breakdowns, and explore word clouds of frequently used terms to gain a deeper understanding of audience engagement. By providing a YouTube video URL, users can generate sentiment analysis reports, visualize sentiment breakdowns, and view a word cloud of frequently used terms.

### Demo Video
[![Video Title](https://i.ytimg.com/an_webp/2vorlPgoayU/mqdefault_6s.webp?du=3000&sqp=CPW3i7wG&rs=AOn4CLDnD-epGrRd9R65T0bwX0I4XW_YAA)](https://youtu.be/2vorlPgoayU)


## Features
- **YouTube Comment Extraction**: Automatically fetch comments from a given YouTube video. Note: The current implementation may have a cap on the number of comments extracted due to YouTube page limitations during automated scrolling.
- **Sentiment Analysis**: Classify comments as Positive, Negative, or Neutral using NLP techniques.
- **Data Cleaning**: Remove irrelevant words and lemmatize text for better sentiment prediction.
- **Word Cloud Generation**: Visualize frequently used words in the comments.
- **Interactive Dashboard**: View sentiment distribution and analyzed comments.

## Installation
Follow these steps to set up the project on your local machine. This app supports Linux, macOS, and Windows operating systems:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/DevanshUpadhyay26/youtube_sentiment_analysis.git
    cd youtube-comment-sentiment
    ```

2. **Create a Virtual Environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Required Packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download NLTK Resources:**
    ```bash
    python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('stopwords'); nltk.download('wordnet')"
    ```

5. **Set Up ChromeDriver:**
   - Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
   - Place the `chromedriver.exe` file in an accessible directory.

6. **Run the Application:**
    ```bash
    python app.py
    ```

7. **Access the Web App:**
   Open your browser and go to [http://localhost:5000](http://localhost:5000).

## Usage
1. **Home Page**: Enter the YouTube video URL in the input form and click on the "Analyze Comments" button.
2. **Results Page**: View sentiment distribution, individual comment analysis, and sentiment scores.
3. **Word Cloud Page**: Visualize the word cloud generated from the cleaned comments.

## Contributing
We welcome contributions to improve this project! Please adhere to the following guidelines:

- Follow coding standards consistent with PEP 8 for Python.
- Include unit tests for any new features or changes.
- Ensure all tests pass before submitting a pull request.
- Document any major changes in the project README. Follow these steps to contribute:

1. Fork the repository.
2. Create a new feature branch:
    ```bash
    git checkout -b feature/YourFeatureName
    ```
3. Commit your changes and push the branch:
    ```bash
    git commit -m "Add your message here"
    git push origin feature/YourFeatureName
    ```
4. Open a Pull Request.

Thank you for your contributions!

---
For any issues or suggestions, please open an issue in the GitHub repository.

