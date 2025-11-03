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
    try:
        data = request.get_json()

        # Extract fields
        date = data.get("date")
        heading = data.get("heading")
        content = data.get("content")
        imglnk = data.get("imglnk")
        
        print(heading, date, content, imglnk)


        # Insert into Supabase
        response = supabase.table("newscard").insert({
            "date": content,
            "heading": date,
            "content": heading,
            "imglnk": imglnk,
            
            }).execute()

        return jsonify({"message": "Card added successfully!", "card": response.data}), 201
    

    except Exception as e:
        return jsonify({"error": str(e)}), 500







if __name__ == "__main__":
    app.run(debug=True)