from flask import Flask, render_template, request
from emotion import (
    load_emotions,
    analyze_sentiment,
    normalized_top_movies,
    normalize_title,
)

# Create Flask
app = Flask(__name__)

# Load emotions dictionary from file
emotions_dict = load_emotions()


@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize sentiment
    sentiment_result = ""

    if request.method == "POST":
        # Extract movie title and review text from the form
        movie_title = request.form.get("movie_title", "").strip()
        text_to_analyze = request.form.get("text_input", "").strip()

        # Normalize the movie title and analyze sentiment of the review
        normalized_user_movie_title = normalize_title(movie_title)
        user_sentiment = analyze_sentiment(text_to_analyze, emotions_dict)

        # Compare user sentiment with general sentiment for the movie
        if normalized_user_movie_title in normalized_top_movies:
            general_sentiment = normalized_top_movies[normalized_user_movie_title]
            if user_sentiment == "negative" and general_sentiment == "positive":
                sentiment_result = "This is a negative review. However, generally, many other people recommend this movie."
            elif user_sentiment == "positive" and general_sentiment == "positive":
                sentiment_result = "Based on this review, I recommend this movie."
            else:
                sentiment_result = (
                    "Based on this review, I do not recommend this movie."
                )
        else:
            # if movie not in the top movies list
            sentiment_result = f"Based on this review, I {'recommend' if user_sentiment == 'positive' else 'do not recommend'} this movie."

    # Render the index page with the sentiment result
    return render_template("index.html", sentiment_result=sentiment_result)


if __name__ == "__main__":
    app.run(debug=True)