import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import client, create_client


url: str = "https://uivlgbwjswwodswogdmh.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVpdmxnYndqc3d3b2Rzd29nZG1oIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE3MzQ1NzQsImV4cCI6MjA3NzMxMDU3NH0.reI9TpS4rzm3aRQUCWLvI6OxFyvrmbSbvnrpAup2wdg"
supabase = create_client(url, key)
app = Flask(__name__)
CORS(app)
# 
# rows = response.data

# print(rows)

@app.route("/")
def init():
    response = supabase.table("newscard").select("*").execute()
    rows = response.data
    return jsonify(rows)



@app.route("/add_card", methods=["POST"])
def add_cards():
    data = request.json
    required_fields = ["heading", "imglnk", "content", "date"]
    for field in required_fields:
        if required_fields not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400
        
    response = supabase.table("newscards").insert({
    "heading": data["heading"],
    "imglnk": data["imglnk"],
    "content": data["content"],
    "date": data["date"]
    }).execute()

    if response.status_code != 201 and response.status_code != 200:
        return jsonify({"error": "Failed to add card", "details": response.data}), 500

    return jsonify({"message": "Card added successfully!", "card": response.data}), 201









if __name__ == "__main__":
    app.run(debug=True)