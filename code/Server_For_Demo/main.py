from flask import Flask, render_template, request, redirect, url_for
import json
import datetime
import time
from twilio.rest import Client
import threading

app = Flask(__name__)
users = []
host_phone_number="" 
last_test_times = {}
last_esp32_alive_time = 0

checking_interval=60 #1 minute - Every 1 minute, partygoersmust go take their BAC test.
grace_interval=90 #90 seconds - After 1 minute 30 seconds, the host will be notified about failure to test.
bac_threshold=0.1 #0.1%

period_of_check=30 #30 seconds
esp32_health_interval = 60 #60 seconds

# Twilio Account SID and Auth Token
account_sid = "x"
auth_token = "x"
client = Client(account_sid, auth_token)

#method to send text messages
def send_text_message(phone_number, message):
    message = client.messages.create(
        body=message,
        from_='+18339011273',
        to=phone_number
    )
    print("Message sent to", phone_number, ":", message.sid)

#message to check BAC levels
def check_bac_levels():
    global last_esp32_alive_time
    while True:

        #iterate through all users
        for user in users:
            phone_number = user['phone']

            last_test_time = last_test_times.get(phone_number) #find last test time

             #checks if it's been 1 minute since last checked
            if (datetime.datetime.now() - last_test_time).total_seconds() >= checking_interval:  
                minutes = round(int((datetime.datetime.now() - last_test_time).total_seconds())/60)

                #first checks if TipsyTracker is Down
                if last_esp32_alive_time is None:
                    send_text_message(user["phone"], "The TipsyTracker System is still down! Please drink responsibly.")
                
                #sends notification to get tested
                else:
                    message="Hey " + user["name"] +" - " + "Please get your BAC levels checked! It's been "+ str(minutes)+ " minutes since you've last tested."
                    send_text_message(phone_number,message)
            
             #check if user has failed repeatedly to get tested
            if (datetime.datetime.now() - last_test_time).total_seconds() >= grace_interval:#checks if it's been 1.5 minutes since last checked (15 minute grace period)
                minutes = round(int((datetime.datetime.now() - last_test_time).total_seconds())/60)
                
                if last_esp32_alive_time is None:
                    send_text_message(host_phone_number,"The TipsyTracker System is still down! Please drink responsibly.")
                else:
                    message =user["name"] + " has failed to test in " + str(minutes) + " minutes"
                    send_text_message(host_phone_number,message)
                 

        time.sleep(period_of_check)  # Check every 30 seconds to see if they haven't tested


#home page routing
@app.route('/', methods=['GET', 'POST'])
def home():
    global host_phone_number
    if request.method == 'POST':
        host_phone_number = request.form['host_phone']
        print('Host phone number submitted:', host_phone_number)
        return redirect(url_for('home'))
    print('Host phone number:', host_phone_number)
    return render_template('home.html', users=users, host_phone=host_phone_number)

#add user routing
@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form["name"]
    phone = request.form["phone"]
    rfid = request.form["rfid"]
    users.append({"name": name, "phone": phone, "rfid": rfid, "breathalyzer": []})
    last_test_times[phone] = datetime.datetime.now()
    return redirect(url_for("home"))

#generating 500 users for demo
@app.route("/generate_500_users", methods=["POST"])
def generate_500_users():
    for i in range(501):
        name = f"User {i+1}"
        phone = f"xxx-xxx-xxxx"
        rfid = "1235"
        users.append({"name": name, "phone": phone, "rfid": rfid, "breathalyzer": []})
    return redirect(url_for("home"))


#add phone routing
@app.route('/add_phone', methods=['POST'])
def add_phone():
    global host_phone_number
    host_phone_number = request.form['host_phone']
    return redirect(url_for('home'))

#routing for data gathering from ESP32
@app.route("/data", methods=["POST"])
def receive_data():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if request.method == 'POST':
        data = request.get_json()
        print(data)
    rfid = data["rfid"].replace(" ", "")
    breathalyzer = data["breathalyzer"]
    if (breathalyzer)<175:
        breathalyzer=0
    else:
        breathalyzer=breathalyzer*0.00028 - 0.00739
    
    if (breathalyzer<0):
        breathalyzer=0

    print(rfid, breathalyzer)
    for user in users:

        #correlates RFID value to user, sends text message with BAC level
        if (user["rfid"]).lower() == rfid:
            user["breathalyzer"].append({"timestamp": timestamp, "value": breathalyzer})
            last_test_times[user["phone"]] = datetime.datetime.now()
            send_text_message(user["phone"], "Hello, your BAC level is: " + str(breathalyzer)+"%")
            if(breathalyzer>bac_threshold):
                message_to_send = user["name"] + " has a high BAC level of " + str(breathalyzer) + "%"
                send_text_message(host_phone_number, message_to_send)

            break
    return "Data received"


#routing for removing user
@app.route("/remove_user", methods=["POST"])
def remove_user():
    rfid = request.args.get("rfid")
    for user in users:
        if user["rfid"] == rfid:
            users.remove(user)
            last_test_times.pop(user["phone"], None)
            break
    return redirect(url_for("home"))


#checks if ESP32 is still alive
def check_esp32_alive():
    global last_esp32_alive_time
    has_been_down=0
    print(last_esp32_alive_time)
    while True:

        #last_esp32_alive_time is set to 0 on startup - so checking
        if last_esp32_alive_time ==0:
            last_esp32_alive_time=datetime.datetime.now()

        #if None, esp32 is down
        if(last_esp32_alive_time is not None):
            time_since_last_esp32_alive = (datetime.datetime.now() - last_esp32_alive_time).total_seconds()
            if time_since_last_esp32_alive > esp32_health_interval:
                #sends notification to all users
                for user in users:
                    send_text_message(user["phone"], "The TipsyTracker System is down! Please drink responsibly.")
                send_text_message(host_phone_number, "The TipsyTracker System is down! Please drink responsibly.")

                print("System Down! Please drink responsibly")
                has_been_down=1

                #set to none, saying it's down
                last_esp32_alive_time = None
            else:
                if (has_been_down==1):
                    print("System Back Up!")
                    for user in users:
                        send_text_message(user["phone"], "The TipsyTracker System is back up!")
                    send_text_message(host_phone_number, "The TipsyTracker System is back up!")
                    has_been_down=0

        time.sleep(5)

#routing for getting alive pings from ESP32
@app.route('/alive', methods=['GET'])
def alive():
    global last_esp32_alive_time
    last_esp32_alive_time = datetime.datetime.now()
    return 'Alive'

#history routing
@app.route("/history")
def history():
    return render_template("history.html", users=users)

#clearing data routing
@app.route('/clear_data', methods=['POST'])
def clear_data():
    global users
    users=[]
    return redirect(url_for('home'))

#settings page
@app.route("/settings")
def settings():
    return render_template("settings.html", bac_threshold = bac_threshold, checking_interval=checking_interval, grace_interval=grace_interval)

#saving settings
@app.route("/save_settings", methods=["POST"])
def save_settings():
    global checking_interval
    global grace_interval
    global bac_threshold

    checking_interval = int(request.form["checking_interval"])
    grace_interval = int(request.form["grace_interval"])
    bac_threshold =  float(request.form["bac_threshold"])

    return redirect(url_for("home"))

#threads
if __name__ == "__main__":
    # Start a new thread to periodically check BAC levels and send text messages
    check_bac_levels_thread = threading.Thread(target=check_bac_levels)
    check_bac_levels_thread.start()

    check_esp32_alive_thread = threading.Thread(target=check_esp32_alive)
    check_esp32_alive_thread.start()

    app.run(host='0.0.0.0', port=5000)
