
/************************************************************************
  4channelRelay12_20241216a
  Robin Greig, 2024.12.16
  Use 4 channel Relay board with built in ESP8266
  To program connect GPIO00 to GND pin & TX, RX, & GND to Raspi
  mqtt keepalive is only 15 seconds so I've added 2 functions
  to check for wifi & mqtt connection at the start of the loop
  mqtt broker: mqtt21.local
  mqtt topics: esp8266/12/nameOfTopic
  Send mqtt 0000 for all off & 1111 for all on, any other digit won't change relay
  Each digit represents a relay (first on left & fourth on right)
  Publish RSSI on MQTT esp8266/12/RSSI
  temperature1 = sensors.getTempCByIndex(0) which is Green/Red DS18B20
  which will publish Battery Temp on MQTT esp8266/12/battTemp
  temperature2 = sensors.getTempCByIndex(1) which is Silver DS18B20
  which will publish Outside Temp on MQTT esp8266/12/outTemp
  Used millis to delay publishing without delaying MQTT loop checking
  Used for loop to sample battery voltage x 3 before publishing
**************************************************************************/
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <string.h>

#define analogPin A0 // ESP8266 Analog Pin ADC0 = A0

//const char* ssid = "Calalta02"; // WiFi name
//const char* password =  "Micr0s0ft2018"; // WiFi password
//const char* ssid = "Calalta03"; // WiFi name
//const char* password =  "Micr0$0ft2024"; // WiFi password
const char* ssid = "TELUS2547"; // WiFi name
const char* password =  "g2299sjk6p"; // WiFi password
const char* mqttServer = "192.168.200.21";
const int mqttPort = 1883;
const char* mqttUser = "otfxknod";
const char* mqttPassword = "nSuUc1dDLygF";

int adcSample = 0; //Varialble to store Sample adc
int adcValue = 0; // Varialbe to store running total of adcSample
int adcAverage = 0; // Variable to store average value of adc
float adcFloat = 0; // Variable to convert ADC value to battery voltage
char adcFloatChar[6]; // Variable to store voltage as a Char

unsigned long previousMillis = 0; // will store last time MQTT published
//const long interval = 5000; // 5 second interval at which to publish MQTT values
//const long interval = 60000; // 60 second interval at which to publish MQTT values
//const long interval = 180000; // 3 minute interval at which to publish MQTT values
const long interval = 300000; // 5 minute interval at which to publish MQTT values

const char *switch01 = "esp8266/12/GPIO"; // MQTT subscribe topic for switch inputs
const char *battVolt = "esp8266/12/battVolt"; // MQTT publish topic for battery voltage
const char *outTemp = "esp8266/12/outTemp"; // MQTT publish topic for outside temperature
const char *battTemp = "esp8266/12/battTemp"; // MQTT publish topic for outside temperature
const char *rssi = "esp8266/12/RSSI"; // MQTT publish topic for signal RSSI

 
WiFiClient espClient;
PubSubClient client(espClient);

int pinNum[4] = {16, 14, 12, 13};
// Initialize Relay 1, GPIO16, WAKE pin as an output
// Initialize Relay 2, GPIO14, SCLK pin as an output
// Initialize Relay 3, GPIO12, MISO pin as an output
// Initialize Relay 4, GPIO13, MOSI pin as an output

// DS18B20

// GPIO where the DS18B20 is connected to
const int oneWireBus = 02;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor
DallasTemperature sensors(&oneWire);

// initialize temp variables
//int numberOfDevices;
//DeviceAddress tempDeviceAddress;
float temperature1 = 0;
float temperature2 = 0;
char *temperatureChar1 = "00.00";
char *temperatureChar2 = "00.00";


void reconnectMQTT() {
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
    // Unique client ID (using ESP8266 macAddress)  
    String client_id = "esp8266-";
    client_id += String(WiFi.macAddress());
    Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 
//    if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {
    if (client.connect(client_id.c_str())) {
      Serial.printf("The client %s is connected to MQTT\n", client_id.c_str());
      String WiFiRSSI = String(WiFi.RSSI());
      Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());
      client.subscribe(switch01); // subscribe to mqtt topic
    } else {
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(500);
    }
  }
}

void reconnectWiFi() {
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void setup() {
 
  Serial.begin(115200);
  for (int i = 0; i < 9; i++){
    pinMode(pinNum[i], OUTPUT);
    digitalWrite(pinNum[i], LOW); 
  }
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
  //sensors.begin();
  //numberOfDevices = sensors.getDeviceCount();
  //Serial.print("Locating devices...");
  //Serial.print("Found   ");
  //Serial.print(numberOfDevices, DEC);
  //Serial.println(" devices");
}
 

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
  Serial.print("Received ansi: ");
  Serial.println(*payload);
  Serial.print("Full Message Arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
  // Switch on Relay 1 & the BuiltInLED if a 1 was received as the first character
  if ((char)payload[0] == '0') {
    digitalWrite(pinNum[0], LOW);   // Turn off Relay 1
  } else if ((char)payload[0] == '1') {
    digitalWrite(pinNum[0], HIGH);  // Turn on Relay 1
  }
  if ((char)payload[1] == '0') {
    digitalWrite(pinNum[1], LOW);   // Turn off Relay 1
  } else if ((char)payload[1] == '1') {
    digitalWrite(pinNum[1], HIGH);  // Turn on Relay 1
  }
  if ((char)payload[2] == '0') {
    digitalWrite(pinNum[2], LOW);   // Turn off Relay 1
  } else if ((char)payload[2] == '1') {
    digitalWrite(pinNum[2], HIGH);  // Turn on Relay 1
  }
  if ((char)payload[3] == '0') {
    digitalWrite(pinNum[3], LOW);   // Turn off Relay 1
  } else if ((char)payload[3] == '1') {
    digitalWrite(pinNum[3], HIGH);  // Turn on Relay 1
  }

  delay(500);
}
  
void loop()
{
  // Connect to WiFi if not connected
  if (WiFi.status() != WL_CONNECTED) {
    reconnectWiFi();
  }

  // Connect to MQTT if not connected
  if(!client.connected()) {
    reconnectMQTT();
  }

  unsigned long currentMillis = millis();
  /* Check to see if it is time to publish MQTT, if the difference between the current
   *  time and the last time > 5 seconds then pubilish again
   */

  if (currentMillis - previousMillis >= interval) {
    // Update previousMillis to current time
    previousMillis = currentMillis;
    // Publish RSSi to esp8266/02/RSSI with retain flag set
    String WiFiRSSI = String(WiFi.RSSI());
    client.publish(rssi,WiFiRSSI.c_str(),"-r");
    sensors.requestTemperatures();
    temperature1 = sensors.getTempCByIndex(0);
    Serial.print("Yellow/Green or Green/Red = battTemp = ");
    Serial.print(temperature1);
    Serial.println("ºC"); 
    sprintf(temperatureChar1,"%.2f", temperature1);
    /* Publish the Battery Temperature to esp8266/02/battTemp with retain flag set */
    client.publish(battTemp, temperatureChar1,"-r"); //publish temp
    temperature2 = sensors.getTempCByIndex(1);
    Serial.print("Blue or Silver = outTemp = ");
    Serial.print(temperature2);
    Serial.println("ºC"); 
    sprintf(temperatureChar2,"%.2f", temperature2);
    /* Publish the Outdoor Temperature to esp8266/02/outTemp with retain flag set */
    client.publish(outTemp, temperatureChar2,"-r"); //publish temp
  }
  client.loop();
  
}
