# 🎬 Movie Recommendation Dataset Collector

A simple Flask web application for collecting real-time movie ratings and reviews to build datasets for Machine Learning and Recommendation System projects.

## ✨ Features

* ⭐ Submit movie ratings (1–5)
* 📝 Write movie reviews
* 🎭 Select genres, platform, and mood tags
* 👍 Recommend or not recommend a movie
* 📊 Live response statistics
* 📥 Export collected data as CSV
* 💾 SQLite database
* 🚀 Easy deployment on Render

## 📂 Project Structure

```
movie-recommender/
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── index.html
└── README.md
```

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open: `http://127.0.0.1:5000`

## 📡 API Endpoints

| Endpoint      | Description           |
| ------------- | --------------------- |
| `/`           | Web interface         |
| `/api/submit` | Submit review         |
| `/api/stats`  | View statistics       |
| `/api/export` | Export dataset as CSV |

## 📊 Dataset Fields

`user_id`, `movie_name`, `rating`, `genres`, `platform`, `moods`, `recommend`, `review`, `timestamp`

---

Built for **Machine Learning**, **Data Mining**, and **Movie Recommendation System** projects.
