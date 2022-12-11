#include <ESP8266WiFi.h>
#include <PubSubClient.h>#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 display = Adafruit_SSD1306();

#define BUTTON_A 0
#define BUTTON_B 16
#define BUTTON_C 2
#define LED      0

#if (SSD1306_LCDHEIGHT != 32)
 #error("Height incorrect, please fix Adafruit_SSD1306.h!");
#endif
 
const char* ssid = "Calalta02"; // Enter your WiFi name
const char* password =  "Micr0s0ft2018"; // Enter WiFi password
const char* mqttServer = "192.168.200.21"; // Enter mqtt server IP
const int mqttPort = 1883; // Enter mqtt port
const char* mqttUser = "otfxknod";
const char* mqttPassword = "nSuUc1dDLygF";

WiFiClient espClient;
PubSubClient client(espClient);
 
void setup() {
 
  Serial.begin(115200);
  delay(1000);
  Serial.println("OLED init");
  // by default, we'll generate the high voltage from the 3.3v line internally! (neat!)
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3C (for the 128x32)
  // init done
  delay(1000);
  Serial.println("OLED begin");
  
  // Show image buffer on the display hardware.
  // Since the buffer is intialized with an Adafruit splashscreen
  // internally, this will display the splashscreen.
  display.display();
  delay(1000);

  // Clear the buffer.
  display.clearDisplay();
  display.display();
  delay(1000);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print("Connecting to ");
    Serial.print(ssid);
    Serial.println(" ......");
    // text display tests
    display.clearDisplay();
    display.setTextSize(2);
    display.setTextColor(WHITE);
    display.setCursor(0,0);
    display.println("Trying");
    display.println(ssid);
    display.display(); // actually display all of the above
  }
  
  Serial.print("Connected to ");
  Serial.println(ssid);
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
//  display.print("IP: ");
  display.print(WiFi.localIP());
  display.print(" ");
//  display.print("RSSI: ");
  display.println(WiFi.RSSI());
  display.display(); // actually display all of the above display.display();
  delay(2000);
 
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
 
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
 
//    if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {
    if (client.connect("ESP8266Client")) {
 
      Serial.println("connected");  
 
    } else {
 
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
 
    }
  }
 
//  client.publish("esp/test", "hello"); //Topic name
  client.publish("esp/test", mqttUser); //Topic name
  client.subscribe("Garden/Pump2");
 
}
 
void callback(char* topic, byte* payload, unsigned int length) {
 
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
 
  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
 
  Serial.println();
  Serial.println("-----------------------");
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.println("Solar");
  for (int i = 0; i < length; i++) {
    display.print((char)payload[i]);
  }
  display.println(" V");
  display.display(); // actually display all of the above
  delay(2000);
 
}
 
void loop() {
  client.loop();
}
