#include <SPI.h>
#include <MFRC522.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>


#define SS_PIN 5
#define RST_PIN 22
#define SENSOR_PIN 35
#define LED_PIN 32

const char* ssid = "esp";
const char* password = "tennisrules";
const char* host = "172.20.10.2";
const int port = 5000;

MFRC522 rfid(SS_PIN, RST_PIN); // create an instance of the MFRC522 object

int sensorValue = 0; // variable to store the sensor value
unsigned long startTime = 0; // variable to store the start time
unsigned long elapsedTime = 0; // variable to store the elapsed time
unsigned long maxValue = 0; // variable to store the maximum sensor value
int sum = 0;
int middle4Sum = 0;
int middle4Count = 0;

unsigned long previousMillis = 0;  // variable to store last time "I'm Alive" message was sent
const long interval = 10000; 



void setup() {
  Serial.begin(9600); // initialize serial communication
  SPI.begin(); // initialize SPI communication

  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("WiFi connected!");
  rfid.PCD_Init(); // initialize the RC522
  pinMode(LED_PIN, OUTPUT);

}

void loop() {
    digitalWrite(LED_PIN, LOW);
    if (millis() - previousMillis >= interval) {
    // send the "I'm Alive" message
     WiFiClient client;
    HTTPClient http;
    http.begin(client, host, port, "/alive"); // specify the server and endpoint
    int httpResponseCode = http.GET(); // send the request
    if (httpResponseCode == 200) {
      Serial.println("Sent 'I'm Alive' message to server");
    } else {
      Serial.println("Failed to send 'I'm Alive' message to server");      // ...
    }
    http.end();
    previousMillis = millis();  // update previousMillis with current time
  }
  // look for new RFID cards
  
  elapsedTime=0;
  startTime=0;
  middle4Sum=0;
  middle4Count=0;
  sensorValue=0;
  if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {
    // print the UID of the card
    Serial.print("UID tag :");
    String rfidContent = "";
    byte letter;
    for (byte i = 0; i < rfid.uid.size; i++) {
      Serial.print(rfid.uid.uidByte[i] < 0x10 ? " 0" : " ");
      Serial.print(rfid.uid.uidByte[i], HEX);
      rfidContent.concat(String(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "));
      rfidContent.concat(String(rfid.uid.uidByte[i], HEX));
    }
    Serial.println();
    Serial.println("Starting test");
     for (int i = 0; i < 4; i++) {
        digitalWrite(LED_PIN, LOW);
        delay(500);
        digitalWrite(LED_PIN, HIGH);
        delay(500);
    }
    digitalWrite(LED_PIN, LOW);


    
    // Record the output of the MQ-3 breathalyzer for a period of 6 seconds
    unsigned long startTime = millis(); // store the start time
    while (millis() - startTime < 6000) {
        sensorValue = analogRead(SENSOR_PIN); // read the sensor value
        sum += sensorValue; // add sensor data to sum
        if (millis() - startTime >= 1000 && millis() - startTime < 5000) { // record the middle 4 seconds
            middle4Sum += sensorValue; // add sensor data to middle 4 sum
            middle4Count++; // increment middle 4 count
        }
    }
    Serial.println();
    // Calculate the average of the middle 4 seconds
    int average = middle4Sum / middle4Count;
    if (average<150){ average = average/3; }
    // Print the calculated average
    Serial.print("Average: ");
    Serial.println(average);

    digitalWrite(LED_PIN, HIGH);
    Serial.println();
    Serial.print("JSON output: [\"");
    Serial.print(rfidContent);
    Serial.print("\", ");
    Serial.print(average);
    Serial.println("]");
    
    DynamicJsonDocument doc(1024);
    doc["rfid"] = rfidContent;
    doc["breathalyzer"] = average;
    String jsonData;
    serializeJson(doc, jsonData);

    
    WiFiClient client;
    HTTPClient http;
    http.begin(client, host, port, "/data"); // specify the server and endpoint
    http.addHeader("Content-Type", "application/json"); // set the content type
    int httpResponseCode = http.POST(jsonData); // send the request
     if (httpResponseCode > 0) {
        String response = http.getString();
        Serial.println(httpResponseCode);
        Serial.println(response);
      } else {
        Serial.print("Error on sending POST: ");
        Serial.println(httpResponseCode);
      }
      http.end();

    Serial.println("Done with test");
      
    for (int i = 0; i < 15; i++) {
      delay(1000);
 
    }
     rfid.PICC_HaltA();
     rfid.PCD_StopCrypto1();
  }
  
 
  delay(1000); // wait for 1 second before reading the sensor again
}
