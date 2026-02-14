#  AI Movie Recommender System

An interactive **content-based movie recommendation system** built using **Natural Language Processing (NLP)** and **cosine similarity**.  
The application analyzes movie metadata and recommends similar movies based on user selection.

Built with **Python, Scikit-learn, and Streamlit**, this project demonstrates a practical implementation of NLP in recommendation engines.

---

 Features

- 🎯 Content-based movie recommendations
- 🔍 Real-time movie search
- ⭐ User rating simulation
- 📊 Sidebar analytics dashboard
- 🎨 Dark Netflix-style UI
- ⚡ Fast cosine similarity engine
- 🌐 Streamlit web interface

---

##  How It Works

1. Movie metadata (overview, genres, cast, keywords, crew) is combined into a single text feature.
2. Text is processed using:
   - Tokenization
   - Stopword removal
   - Stemming (NLTK)
3. The processed text is converted into numerical vectors using **CountVectorizer**.
4. **Cosine similarity** is calculated between all movie vectors.
5. When a user selects a movie, the system:
   - Finds similar vectors
   - Ranks movies by similarity
   - Displays top recommendations.

---

##  Tech Stack

| Category | Tools |
|---------|------|
| Language | Python |
| NLP | NLTK, Scikit-learn |
| ML Method | CountVectorizer, Cosine Similarity |
| Web App | Streamlit |
| Data Handling | Pandas |
| Deployment | Streamlit Cloud |

---

##  Project Structure

movie-recommender/
│
├── app.py
├── movies_dict.pkl
├── similarity.pkl
├── requirements.txt
└── README.md


---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

2. Install dependencies
pip install -r requirements.txt

3. Run the Streamlit app
streamlit run app.py

The app will open in your browser.
🖥 Example Workflow
Search or select a movie
Provide a rating (optional)
Click Recommend Movies
View similar movie suggestions with similarity scores

📊 Core Algorithm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(tags).toarray()

similarity = cosine_similarity(vectors)

🌐 Deployment (Streamlit Cloud)
Push the project to GitHub
Go to: https://streamlit.io/cloud
Click New App
Select your repository
Choose app.py
Click Deploy

🎯 Use Cases
Movie recommendation platforms
NLP learning projects
Portfolio or internship submissions
Streamlit dashboard demos

🔮 Future Improvements
Poster integration using TMDB API
Collaborative filtering
Genre-based filtering
Trending movies section
User login & watchlist

👨‍💻 Author
Ayush Singh
AI & ML Enthusiast
GitHub: https://github.com/ayu-sh87
LinkedIn: https://www.linkedin.com/in/ayu108

⭐ If you like this project
Give it a star on GitHub and share your feedback!


