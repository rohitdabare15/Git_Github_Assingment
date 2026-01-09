from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

# MongoDB Atlas connection
MONGO_URI = "mongodb+srv://Rohit:1234@cluster0.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client.mydb
collection = db.users

@app.route("/", methods=["GET", "POST"])
def form():
    error = None

    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            # Insert into MongoDB
            collection.insert_one({
                "name": name,
                "email": email
            })

            return redirect(url_for("success"))

        except PyMongoError as e:
            error = str(e)

    return render_template("form.html", error=error)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
