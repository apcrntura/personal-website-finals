from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["*"])  # In production, replace * with your Vercel frontend URL

# Supabase client
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL and SUPABASE_KEY else None

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Rae Allen Tura - Personal Website API", "status": "running"})


@app.route("/comments", methods=["GET"])
def get_comments():
    """GET all guestbook comments, newest first"""
    try:
        response = supabase.table("comments") \
            .select("*") \
            .order("created_at", desc=True) \
            .execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/comments", methods=["POST"])
def post_comment():
    """POST a new guestbook comment"""
    try:
        body = request.get_json()

        if not body:
            return jsonify({"error": "Request body is required"}), 400

        name = body.get("name", "").strip()
        message = body.get("message", "").strip()

        if not name or not message:
            return jsonify({"error": "Name and message are required"}), 400

        if len(name) > 100:
            return jsonify({"error": "Name is too long (max 100 chars)"}), 400

        if len(message) > 1000:
            return jsonify({"error": "Message is too long (max 1000 chars)"}), 400

        data = {
            "name": name,
            "message": message,
        }

        response = supabase.table("comments").insert(data).execute()
        return jsonify(response.data[0]), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
