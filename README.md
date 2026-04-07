# Movie Recommendation Dataset Collector

A Flask web app to collect real-time movie review data from friends for your AIML recommendation system project.

## Project Structure
```
movie-recommender/
├── app.py              # Flask backend + SQLite DB
├── requirements.txt    # Python dependencies
├── Procfile            # Render/Heroku start command
├── README.md
└── templates/
    └── index.html      # Full frontend form
```

---

## Deploy to Render (Free) — Step by Step

### Step 1: Push to GitHub
1. Create a new repo at https://github.com/new (name it `movie-recommender`)
2. Upload all files from this folder to that repo (drag & drop works)

### Step 2: Deploy on Render
1. Go to https://render.com and sign up (free)
2. Click **New → Web Service**
3. Connect your GitHub account → select your `movie-recommender` repo
4. Fill in settings:
   - **Name**: movie-recommender (or any name)
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free
5. Click **Create Web Service**
6. Wait ~2 minutes for build

### Step 3: Share the link!
Render gives you a URL like: `https://movie-recommender-xxxx.onrender.com`
Share this with your friends — everyone's responses go to the same database!

---

## Features
- Real-time response counter (auto-refreshes every 15 seconds)
- SQLite database (persists on Render's disk)
- Export all data as CSV with one click
- Fields: User ID, Movie Name, Rating (1-5★), Genre, Platform, Mood Tags, Recommend, Review

## Export Data for ML
Visit `/api/export` or click the **Export CSV** button in the Dataset tab.

CSV columns:
```
id, timestamp, user_id, movie_name, rating, genres, platform, moods, recommend, review
```

## Load Data in Python
```python
import pandas as pd

df = pd.read_csv("movie_dataset.csv")

# Quick analysis
print(df.groupby("movie_name")["rating"].mean().sort_values(ascending=False))
print(df["recommend"].value_counts())

# For collaborative filtering
pivot = df.pivot_table(index="user_id", columns="movie_name", values="rating")
print(pivot)
```

## API Endpoints
| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Main form UI |
| `/api/submit` | POST | Submit a response |
| `/api/stats` | GET | Live stats + recent 50 rows |
| `/api/export` | GET | Download full CSV |

---

## Tips for Better Dataset
- Ask 20+ friends to fill it
- Encourage multiple submissions (different movies)
- Keep movie names consistent (use exact titles)
- Collect at least 5 ratings per movie for meaningful recommendations
