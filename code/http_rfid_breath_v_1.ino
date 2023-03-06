#include <SPI.h>
#include <MFRC522.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>


#define SS_PIN 5
#define RST_PIN 22
#define SENSOR_PIN 35

const char* ssid = "esp";
const char* password = "tennisrules";
const char* host = "172.20.10.4";
const int port = 5000;

MFRC522 rfid(SS_PIN, RST_PIN); // create an instance of the MFRC522 object

int sensorValue = 0; // variable to store the sensor value
unsigned long startTime = 0; // variable to store the start time
unsigned long elapsedTime = 0; // variable to store the elapsed time
unsigned long maxValue = 0; // variable to store the maximum sensor value

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


}

unsigned long previousMillis = 0;  // variable to store last time "I'm Alive" message was sent
const long interval = 30000; 

void loop() {
  
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
  maxValue=0;
  sensorValue=0;
  if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {
    // print the UID of the card
    Serial.print("UID tag :");
    maxValue=10;
    String rfidContent = "";
    byte letter;
    for (byte i = 0; i < rfid.uid.size; i++) {
      Serial.print(rfid.uid.uidByte[i] < 0x10 ? " 0" : " ");
      Serial.print(rfid.uid.uidByte[i], HEX);
      rfidContent.concat(String(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "));
      rfidContent.concat(String(rfid.uid.uidByte[i], HEX));
    }
    Serial.println();
    Serial.println("Please wait 3 seconds before starting the breathalyzer exam");
    delay(3000); // wait for 3 seconds
    Serial.println("Breathalyzer readings:");
    startTime = millis(); // store the start time
    while (elapsedTime < 1000) { // loop for 5 seconds
      sensorValue = analogRead(SENSOR_PIN); // read the sensor value
      if (sensorValue > maxValue) { // update the maximum value
        maxValue = sensorValue;
      }
      Serial.print(sensorValue); // print the sensor value to the serial monitor
      Serial.print(", ");
      elapsedTime = millis() - startTime; // calculate the elapsed time
    }
    Serial.println();
    Serial.print("JSON output: [\"");
    Serial.print(rfidContent);
    Serial.print("\", ");
    Serial.print(maxValue);
    Serial.println("]");
    
    DynamicJsonDocument doc(1024);
    doc["rfid"] = rfidContent;
    doc["breathalyzer"] = maxValue;
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
    
  }
  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
  delay(1000); // wait for 1 second before reading the sensor again
}
