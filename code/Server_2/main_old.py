from flask import Flask, render_template, request, redirect, url_for
import json
import datetime

app = Flask(__name__)
users = []

@app.route("/")
def home():
    return render_template("home.html", users=users)

@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form["name"]
    phone = request.form["phone"]
    rfid = request.form["rfid"]
    users.append({"name": name, "phone": phone, "rfid": rfid, "breathalyzer":[]})
    return redirect(url_for("home"))

@app.route("/data", methods=["POST"])
def receive_data():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if request.method == 'POST':
        data = request.get_json()
        print(data)
    rfid = data["rfid"].replace(" ","")
    breathalyzer = data["breathalyzer"]
    print(rfid, breathalyzer)
    for user in users:
        if user["rfid"] == rfid:
            user["breathalyzer"].append({"timestamp": timestamp, "value": breathalyzer})
            break
    return "Data received"

@app.route("/remove_user", methods=["POST"])
def remove_user():
    rfid = request.args.get("rfid")
    for user in users:
        if user["rfid"] == rfid:
            users.remove(user)
            break
    return redirect(url_for("home"))

@app.route("/history")
def history():
    return render_template("history.html", users=users)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
