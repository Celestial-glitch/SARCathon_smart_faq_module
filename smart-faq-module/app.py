import json
from flask import Flask, request, render_template, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)  # Corrected __name__

# Load FAQ data
with open('faqs.json') as f:
    faqs = json.load(f)

# Extract the FAQ questions
questions = [faq['question'] for category in faqs.values() for faq in category]

# Initialize the TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(questions)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_query = request.json.get('query')
    print(f"Received query: {user_query}")

    # Use the vectorizer to transform the user query
    user_vector = vectorizer.transform([user_query])
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()

    # Get the top 3 matches
    top_indices = similarity_scores.argsort()[-3:][::-1]

    matches = []
    for index in top_indices:
        count = 0
        for category in faqs.values():
            for faq in category:
                if count == index:
                    matches.append(faq)
                count += 1

    if not matches:
        return jsonify({"error": "No relevant FAQs found"}), 404

    return jsonify(matches)

if __name__ == '__main__':  # Corrected __name__
    app.run(debug=True)

