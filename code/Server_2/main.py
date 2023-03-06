from flask import Flask, render_template, request, redirect, url_for
import json
import datetime
import time
from twilio.rest import Client
import threading

app = Flask(__name__)
users = []
last_test_times = {}
last_esp32_alive_time = 0

# Twilio Account SID and Auth Token
account_sid = "ACaed10979a1ae496a080957744ea48002"
auth_token = "762f0dfe9180fb586bbc220401fa2643"
client = Client(account_sid, auth_token)

def send_text_message(phone_number, message):
    message = client.messages.create(
        body=message,
        from_='+18339011273',
        to=phone_number
    )
    print("Message sent to", phone_number, ":", message.sid)

def check_bac_levels():
    while True:
        for user in users:
            phone_number = user['phone']
            last_test_time = last_test_times.get(phone_number)

            if (datetime.datetime.now() - last_test_time).total_seconds() >= 1800:   #checks if it's been 30 minutes since last checked
                minutes = round(int((datetime.datetime.now() - last_test_time).total_seconds())/60)
                message="Hey " + user["name"] +" - " + "Please get your BAC levels checked! It's been "+ str(minutes)+ " minutes since you've last tested."
                send_text_message(phone_number,message)

        time.sleep(300)  # Check every 5 minutes to see if they haven't tested


@app.route("/")
def home():
    return render_template("home.html", users=users)


@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form["name"]
    phone = request.form["phone"]
    rfid = request.form["rfid"]
    users.append({"name": name, "phone": phone, "rfid": rfid, "breathalyzer": []})
    last_test_times[phone] = datetime.datetime.now()
    return redirect(url_for("home"))


@app.route("/data", methods=["POST"])
def receive_data():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if request.method == 'POST':
        data = request.get_json()
        print(data)
    rfid = data["rfid"].replace(" ", "")
    breathalyzer = data["breathalyzer"]
    print(rfid, breathalyzer)
    for user in users:
        if user["rfid"] == rfid:
            user["breathalyzer"].append({"timestamp": timestamp, "value": breathalyzer})
            last_test_times[user["phone"]] = datetime.datetime.now()
            send_text_message(user["phone"], "Hello, your BAC level is: " + str(breathalyzer))
            break
    return "Data received"


@app.route("/remove_user", methods=["POST"])
def remove_user():
    rfid = request.args.get("rfid")
    for user in users:
        if user["rfid"] == rfid:
            users.remove(user)
            last_test_times.pop(user["phone"], None)
            break
    return redirect(url_for("home"))


def check_esp32_alive():
    global last_esp32_alive_time
    has_been_down=0
    while True:
        if last_esp32_alive_time ==0:
            last_esp32_alive_time=datetime.datetime.now()

        if(last_esp32_alive_time is not None):
            time_since_last_esp32_alive = (datetime.datetime.now() - last_esp32_alive_time).total_seconds()
            if time_since_last_esp32_alive > 120:
                for user in users:
                    send_text_message(user["phone"], "The TipsyTracker System is down! Please drink responsibly.")

                print("System Down! Please drink responsibly")
                has_been_down=1

                last_esp32_alive_time = None
            else:
                if (has_been_down==1):
                     print("System Back Up!")
                     send_text_message(user["phone"], "The TipsyTracker System is back up!")
                     has_been_down=0
        time.sleep(1)


@app.route('/alive', methods=['GET'])
def alive():
    global last_esp32_alive_time
    last_esp32_alive_time = datetime.datetime.now()
    return 'Alive'


@app.route("/history")
def history():
    return render_template("history.html", users=users)

@app.route('/clear_data', methods=['POST'])
def clear_data():
    global users
    users=[]
    return redirect(url_for('home'))

if __name__ == "__main__":
    # Start a new thread to periodically check BAC levels and send text messages
    check_bac_levels_thread = threading.Thread(target=check_bac_levels)
    check_bac_levels_thread.start()

    check_esp32_alive_thread = threading.Thread(target=check_esp32_alive)
    check_esp32_alive_thread.start()

    app.run(host='0.0.0.0', port=5000)
