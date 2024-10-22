# Smart FAQ module

A Smart FAQ Module built with Flask, HTML, CSS, and JavaScript that helps users quickly retrieve relevant FAQs based on their queries. The project leverages TF-IDF vectorization and cosine similarity to improve the accuracy of question matching.


## Features

- User-friendly interface: A simple and intuitive search bar for querying FAQs.
- Real-time search: Provides relevant answers based on user input instantly.
- Machine learning for matching: Uses TF-IDF vectorization and cosine similarity to find the most relevant FAQs.
- Dynamic response rendering: JavaScript fetches and displays results dynamically without reloading the page.
- Modular code: HTML, CSS, and Python logic are well-structured and separated for easy maintenance.


## Technology used
- Frontend: HTML, CSS, JavaScript
- Backend: Python with Flask
- Machine Learning: Scikit-learn (TF-IDF and cosine similarity)
- JSON: FAQ data stored in faqs.json
## How to Run the Project
1. Clone the repository:
git clone https://github.com/your-username/smart-faq-module.git
cd smart-faq-module

2. Install dependencies:
Make sure you have Python installed. 
Then run: pip install Flask scikit-learn

3. Run the Flask server:
python app.py

4. Access the application:
Open your browser and go to:
http://127.0.0.1:5000



## File Structure:
- smart-faq-module/

- ├── templates/        # Contains HTML files
-  └── index.html
- ├── faqs.json         # JSON file with FAQ data
- ├── styles.css        # CSS for styling the UI
- ├── app.py            # Flask backend
- └── README.md         # Project description
ng README (1).md…]()
