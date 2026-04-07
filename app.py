from flask import Flask, request, jsonify, render_template, send_file
import sqlite3, csv, io, os
from datetime import datetime

app = Flask(__name__)
DB = "responses.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS responses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                user_id TEXT,
                movie_name TEXT,
                rating INTEGER,
                genres TEXT,
                platform TEXT,
                moods TEXT,
                recommend TEXT,
                review TEXT
            )
        """)
        conn.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/submit", methods=["POST"])
def submit():
    data = request.json
    required = ["user_id", "movie_name", "rating", "recommend"]
    for field in required:
        if not data.get(field):
            return jsonify({"error": f"Missing field: {field}"}), 400
    with get_db() as conn:
        conn.execute("""
            INSERT INTO responses (timestamp, user_id, movie_name, rating, genres, platform, moods, recommend, review)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data["user_id"].strip(),
            data["movie_name"].strip(),
            int(data["rating"]),
            data.get("genres", ""),
            data.get("platform", ""),
            data.get("moods", ""),
            data["recommend"],
            data.get("review", "").strip()
        ))
        conn.commit()
    return jsonify({"success": True})

@app.route("/api/stats")
def stats():
    with get_db() as conn:
        total = conn.execute("SELECT COUNT(*) FROM responses").fetchone()[0]
        avg = conn.execute("SELECT AVG(rating) FROM responses").fetchone()[0]
        movies = conn.execute("SELECT COUNT(DISTINCT LOWER(movie_name)) FROM responses").fetchone()[0]
        recent = conn.execute(
            "SELECT user_id, movie_name, rating, recommend, timestamp FROM responses ORDER BY id DESC LIMIT 50"
        ).fetchall()
    return jsonify({
        "total": total,
        "avg_rating": round(avg, 1) if avg else None,
        "unique_movies": movies,
        "recent": [dict(r) for r in recent]
    })

@app.route("/api/export")
def export():
    with get_db() as conn:
        rows = conn.execute("SELECT * FROM responses ORDER BY id").fetchall()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["id","timestamp","user_id","movie_name","rating","genres","platform","moods","recommend","review"])
    for row in rows:
        writer.writerow(list(row))
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="movie_dataset.csv"
    )

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
