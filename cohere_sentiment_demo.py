# cohere_sentiment_demo.py
#
# A tiny demo that uses Cohere's Chat API to classify the sentiment
# of a few short product reviews as Positive, Negative, or Neutral.
#
# HOW TO RUN THIS (step by step):
#
# 1. Install the Cohere Python package. Open a terminal and run:
#       pip install cohere
#
# 2. Get your free Trial API key:
#       - Go to https://dashboard.cohere.com
#       - Log in (you already have an account)
#       - In the left sidebar, click "API Keys"
#       - Copy your Trial key (it's free, no card needed for this)
#
# 3. Paste your key below, where it says "PASTE_YOUR_KEY_HERE"
#
# 4. Run this file:
#       python cohere_sentiment_demo.py
#
# 5. You should see each review printed with its sentiment label.
#    Take a screenshot or copy the output, that's your proof it works.

import cohere

# Step 3: paste your Cohere Trial API key between the quotes below
API_KEY = "PASTE_YOUR_KEY_HERE"

co = cohere.ClientV2(api_key=API_KEY)

# A few example reviews to classify. Feel free to change these
# to your own sentences before you run it.
reviews = [
    "This laptop is amazing, it never slows down and the battery lasts all day.",
    "Terrible experience, the package arrived broken and support never replied.",
    "It's an okay product. Does what it says, nothing more, nothing less.",
]

print("Cohere Sentiment Classifier Demo")
print("=" * 40)

for review in reviews:
    # We ask the Command model to classify the review in one word.
    prompt = (
        "Classify the sentiment of this product review as exactly one "
        "word: Positive, Negative, or Neutral. "
        f"Review: \"{review}\""
    )

    response = co.chat(
        model="command-r-08-2024",
        messages=[{"role": "user", "content": prompt}],
    )

    sentiment = response.message.content[0].text.strip()

    print(f"\nReview: {review}")
    print(f"Sentiment: {sentiment}")

print("\nDone! This confirms your Cohere API key and connection work.")
