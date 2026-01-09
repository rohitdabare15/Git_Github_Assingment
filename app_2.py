from flask import Flask, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://<username>:<password>@cluster.mongodb.net/")
db = client.todo_db
collection = db.items

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form["itemName"]
    item_description = request.form["itemDescription"]

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
