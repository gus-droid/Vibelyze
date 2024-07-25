import string
import re


def load_emotions():
    # Initialize an empty dictionary to store emotion data
    emotions_dict = {}

    # Open emotions.txt file
    with open("emotions.txt", "r") as file:
        # Iterate through each line in the file
        for line in file:
            # Skip lines without a colon or empty lines
            if ":" not in line or line.strip() == "":
                continue

            # Split each line at the colon to separate the word from the emotion
            word, emotion = line.strip().split(":")

            # Add the word and its emotion to the dictionary, stripping any leading/trailing whitespace
            emotions_dict[word.strip()] = emotion.strip()

    # testing for debugging
    # print("Emotions Dictionary:", emotions_dict)

    # Return the populated dictionary
    return emotions_dict


# Helper function for handling Roman numerals in movie titles
def roman_to_number(roman):
    # Define a dictionary matching Roman numerals to their integer values
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # Initialize a result variable to accumulate the total value
    result = 0

    # Iterate through each character in the Roman numeral string
    for i, c in enumerate(roman):
        # Check if the current numeral is smaller than the next one, indicating a subtractive pair
        if (i + 1) < len(roman) and roman_numerals[c] < roman_numerals[roman[i + 1]]:
            # Subtract the value of the current numeral from the result
            result -= roman_numerals[c]
        else:
            # Add the value of the current numeral to the result
            result += roman_numerals[c]

    # Return the total value of the Roman numeral
    return result


def number_to_roman(num):
    # List of tuples containing Roman numeral symbols and their corresponding values
    val = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    # Initialize empty list to store Roman numerals
    res = []

    # Iterate through the tuple list and make Roman numeral string
    for n, r in val:
        # Use divmod to get the quotient and the remainder
        # Quotient tells how many times the Roman numeral symbol should be repeated
        (d, num) = divmod(num, n)
        # Append the repeated Roman numeral symbol to the result list
        res.append(r * d)

    # Join the list of Roman numeral symbols into a single string
    return "".join(res)


def normalize_title(title):
    # Convert title to lowercase
    title = title.lower()

    # Remove colons and replace hyphens with spaces for consistency
    title = title.replace(":", "").replace("-", " ")

    # Dictionary to convert word numbers to number
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10",
    }

    # Replace all word numbers in the title with their numerical equivalents
    for word, number in numbers.items():
        title = title.replace(word, number)

    # List of Roman numerals to look for in the title
    romans = ["II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

    # Convert any Roman numerals in the title to numbers
    for roman in romans:
        if roman.lower() in title:
            number = roman_to_number(roman)
            title = title.replace(roman.lower(), number_to_roman(number))

    # Remove extra spaces and return the normalized title
    title = " ".join(title.split())

    return title


def analyze_sentiment(text, emotions_dict):
    # Lowercase text and remove punctuation except slashes
    text = text.lower().translate(
        str.maketrans("", "", string.punctuation.replace("/", ""))
    )

    # Regular expression to find ratings like "8/10"
    rating_pattern = re.compile(r"(\d+)/10")
    rating_match = rating_pattern.search(text)

    # If a rating is found, use it to determine sentiment
    if rating_match:
        rating = int(rating_match.group(1))
        return "positive" if rating >= 6 else "negative"

    # If no rating, analyze sentiment based on words in text
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    positive_count, negative_count = 0, 0

    # Count positive and negative words based on emotions dictionary
    for word in words:
        if word in emotions_dict:
            if emotions_dict[word] == "positive":
                positive_count += 1
            elif emotions_dict[word] == "negative":
                negative_count += 1

    # Determine sentiment
    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"


# Top movies list
top_movies = {
    "The Shawshank Redemption": "positive",
    "The Godfather": "positive",
    "The Dark Knight": "positive",
    "The Godfather Part II": "positive",
    "12 Angry Men": "positive",
    "Schindler's List": "positive",
    "The Lord of The Rings: The Return of the King": "positive",
    "Pulp Fiction": "positive",
    "The Lord of The Rings: The Fellowship of the Ring": "positive",
    "The Good, the Bad, and the Ugly": "positive",
    "Forrest Gump": "positive",
    "Fight Club": "positive",
    "The Lord of The Rings: The Two Towers": "positive",
    "Inception": "positive",
    "Star Wars: Episode V - The Empire Strikes Back": "positive",
    "The Matrix": "positive",
    "GoodFellas": "positive",
    "One Flew Over the Cuckoo's Nest": "positive",
    "Se7en": "positive",
    "It's a Wonderful Life": "positive",
    "Seven Samurai": "positive",
    "Interstellar": "positive",
    "The Silence of the Lambs": "positive",
    "Saving Private Ryan": "positive",
    "City of God": "positive",
}

# Create a dictionary of normalized movie titles with their corresponding sentiments
normalized_top_movies = {
    normalize_title(title): sentiment for title, sentiment in top_movies.items()
}