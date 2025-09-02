import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        port=os.environ.get("DB_PORT", 5432),
    )
    return conn

@app.route("/")
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT NOW();")  # Simple query to test connection
        result = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"server_time": result[0].isoformat()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
