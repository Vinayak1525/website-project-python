from flask import Flask, render_template, jsonify
from database import load_gameslist_from_db

app = Flask(__name__)

# HARD CODDING THE DATA

# home_list = [
#     {"id": 1, "title": "Dota2", "location": "Steam", "cost": "free to play"},
#     {"id": 2, "title": "Warframe", "location": "Steam", "cost": "free to play"},
#     {"id": 3, "title": "Fortnite", "location": "Epic Games", "cost": "free to play"},
#     {"id": 4, "title": "Crusader Kings 3", "location": "Steam", "cost": "50$"},
# ]


# HAD TO IMPORT ENGINE FROM DATABASE  #GETTING DATA FROM THE DATABASE


# INITIAL PAGE


@app.route("/")
def hello_world():
    games_data = load_gameslist_from_db()
    return render_template("home.html", games=games_data, website="BaneNZ")


# DIFFERENCE BETWEEN CREATING AN HTML END-POINT AND A JSON END-POINT
# USE render_template for HTML and Jsonify for JSON


@app.route("/api/games")
def list_games():
    return jsonify(home_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
