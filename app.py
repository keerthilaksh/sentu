from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
sid = SentimentIntensityAnalyzer()

def review_rating(string):
    scores = sid.polarity_scores(string)
    positive = scores['pos']
    negative = scores['neg']
    neutral = scores['neu']
    total = positive + negative

    if total == 0:
        return "Neutral"
    else:
        positive_percentage = (positive / total) * 100
        negative_percentage = (negative / total) * 100
        return {
            "Positive": f"{positive_percentage:.2f}%",
            "Negative": f"{negative_percentage:.2f}%"
        }

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        review = request.form['review']
        result = review_rating(review)
        return render_template('index.html', review=review, result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

