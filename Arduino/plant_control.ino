#include <WiFiNINA.h>
#include <ArduinoHttpClient.h>
#include <Arduino_JSON.h>
#include "arduino_secrets.h"

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
/////// WiFi Settings ///////
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;

char serverAddress[] = "54.198.83.230";  // server address
int port = 80;

WiFiClient wifi;
HttpClient client = HttpClient(wifi, serverAddress, port);
int status = WL_IDLE_STATUS;
int hour;
int minute;
int second;

void setup() {
  Serial.begin(9600);
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to Network named: ");
    Serial.println(ssid);  // print the network name (SSID);

    // Connect to WPA/WPA2 network:
    status = WiFi.begin(ssid, pass);
  }

  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);
  pinMode(2, OUTPUT);
  pinMode(x, OUTPUT);
  int brightness_val = 0;
}

void loop() {
  /*
  Serial.println("making POST request for switch val");
  client.beginRequest();
  client.post("/switch");
  client.endRequest();

  int statusCode = client.responseStatusCode();
  JSONVar switchRes = JSON.parse(client.responseBody());
  Serial.print("Status code: ");
  Serial.println(statusCode);
  long switch_val = switchRes["switch"];
  */

  /*
  if (switch_val == "true"){
    Serial.println("switch is on");
    digitalWrite(x, HIGH);

    Serial.println("making POST request for slider val");
    client.beginRequest();
    client.post("/brightness");
    client.endRequest();

    // read the status code and body of the response
    int statusCode = client.responseStatusCode();
    JSONVar sliderRes = JSON.parse(client.responseBody());
    Serial.print("Status code: ");
    Serial.println(statusCode);
    long responseval = sliderRes["slider"].toInt();
    brightness_val = map(responseval, 0, 100, 0, 255);
  }
  */
 /*
  else{
    digitalWrite(x, LOW);
    Serial.print("Switch is off")
  }
  */
  Serial.println("making GET request for time");
  client.beginRequest();
  client.get("/time");
  client.endRequest();
  Serial.println("Parse response and store in hour, minute, second");
  int statusCode = client.responseStatusCode();
  JSONVar timeRes = JSON.parse(client.responseBody());
  Serial.print("Status code: ");
  Serial.println(statusCode);
  hour = timeRes["hour"];
  minute = timeRes["minute"];
  second = timeRes["second"];
  

  /*
  Serial.print("Writing value: ");
  Serial.println(brightness_val);
  analogWrite(2, brightness_val);
  delay(1000);
  */
}