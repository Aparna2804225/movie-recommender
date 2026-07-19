# 🎬 Movie Recommendation Dataset Collector

A lightweight Flask web application for collecting **real-time movie reviews and ratings** from multiple users. The collected dataset can be directly used for building and training **Machine Learning** and **Recommendation System** models such as Collaborative Filtering, Content-Based Filtering, or Hybrid Recommenders.

---

# ✨ Features

- 🎥 Submit movie reviews through a clean web interface
- ⭐ Rate movies from 1–5 stars
- 📝 Write detailed reviews
- 😊 Add mood tags (Happy, Emotional, Thriller, etc.)
- 🎭 Select genres and streaming platforms
- 👍 Recommend or not recommend the movie
- 👥 Supports multiple users
- 📊 Live response statistics
- 📥 Export complete dataset as CSV
- 💾 SQLite database (no external database required)
- 🚀 Easy deployment on Render or Heroku

---

# 📂 Project Structure

```
movie-recommender/
│
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Procfile               # Deployment configuration
├── README.md
│
├── templates/
│   └── index.html         # Frontend UI
│
└── movie_reviews.db       # SQLite database (created automatically)
```

---

# 🛠 Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Pandas (for analysis)

---

# 🚀 Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/movie-recommender.git

cd movie-recommender
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 🌐 Deploy on Render

## Step 1

Push the project to GitHub.

## Step 2

Create a **New Web Service** on Render.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

Choose the **Free Instance** and deploy.

After deployment you'll receive a URL like

```
https://movie-recommender.onrender.com
```

Share this link with friends so everyone contributes to the same dataset.

---

# 📊 Dataset Schema

Each submission stores the following information:

| Field | Description |
|--------|-------------|
| id | Auto-generated ID |
| timestamp | Submission time |
| user_id | User identifier |
| movie_name | Movie title |
| rating | Rating (1–5) |
| genres | Selected genres |
| platform | OTT platform |
| moods | Mood tags |
| recommend | Yes / No |
| review | User review |

---

# 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main web interface |
| `/api/submit` | POST | Submit movie review |
| `/api/stats` | GET | Live statistics |
| `/api/export` | GET | Download CSV dataset |

---

# 📥 Export Dataset

Download the complete dataset by visiting:

```
/api/export
```

or by clicking the **Export CSV** button in the application.

---

# 📈 Using the Dataset for Machine Learning

```python
import pandas as pd

df = pd.read_csv("movie_dataset.csv")

# Average movie ratings
print(df.groupby("movie_name")["rating"].mean())

# Recommendation count
print(df["recommend"].value_counts())

# User-Movie matrix
pivot = df.pivot_table(
    index="user_id",
    columns="movie_name",
    values="rating"
)

print(pivot)
```

---

# 🧠 Ideal Use Cases

- Collaborative Filtering
- Content-Based Recommendation
- Hybrid Recommendation Systems
- Data Mining Projects
- Machine Learning Coursework
- Sentiment Analysis
- User Preference Analysis

---

# 📊 Recommended Dataset Size

For better recommendation performance:

- 👥 20–100 users
- 🎬 100+ unique movies
- ⭐ At least 5–10 ratings per movie
- 📝 Encourage detailed reviews
- 🎭 Keep movie titles consistent

---

# 🤝 Contributing

Contributions are welcome!

You can improve the project by:

- Adding authentication
- Improving UI/UX
- Supporting movie posters
- Integrating TMDB API
- Adding analytics dashboard
- Docker support
- Recommendation visualization

---

# 📄 License

This project is released under the MIT License.

Feel free to use, modify, and distribute it for educational or personal projects.

---

# ⭐ Support

If you found this project helpful:

⭐ Star the repository

🍴 Fork it

📢 Share it with your friends

Your contributions help create a larger and better movie recommendation dataset.
