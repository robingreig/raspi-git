// GPIO16 connect to Reset to wagke up
#include <ESP8266WiFi.h> 
#include <PubSubClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <string.h>

// DS18B20

// GPIO where the DS18B20 is connected to
const int oneWireBus = 13;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqtt_broker = "192.168.200.21"; 

const char *topic1 = "esp8266/04/temp";

const char *topic2 = "esp8266/04/RSSI";

const char *topic3 = "esp8266/04/mac";

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient); 

// LED to turn on when connected
#define LED 2

// initialize temp variable
float temperatureC = 0;
//char *tempChar = "00.00"; // temp needs to be char for mqtt
char tempChar[6]; // temp needs to be char for mqtt
char signal[6]; // RSSI signal needs to be char for mqtt
char mac[18]; // mac address needs to be char for mqtt

void setup() { 

  // Test WDT during Sleep
  ESP.wdtDisable();
  
  Serial.begin(115200); // Start Serial Monitor
  
  sensors.begin(); // Start the DS18B20 sensor

  pinMode(LED, OUTPUT); // setup onboard LED as output

  WiFi.begin(ssid, password); // connecting to the WiFi network 

  while (WiFi.status() != WL_CONNECTED) { 

      // Test WDT & Feed
      ESP.wdtFeed();

      delay(500); 

      Serial.println("Connecting to WiFi.."); 

  } 

  Serial.println("Connected to the WiFi network"); 
  // turn on onboard led
  digitalWrite(LED, HIGH);

  //connecting to a mqtt broker 

  client.setServer(mqtt_broker, mqtt_port);


  while (!client.connected()) {

      // Test WDT & Feed
      ESP.wdtFeed();

      String client_id = "esp8266-"; 

      String WiFiRSSI = String(WiFi.RSSI());

      Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());

      strcpy(signal, WiFiRSSI.c_str());

      client_id += String(WiFi.macAddress());

      Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 

      strcpy(mac, (String(WiFi.macAddress()).c_str()));

//      if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) { 
      if (client.connect(client_id.c_str())) { 

          Serial.println("Mqtt broker connected"); 
          digitalWrite(LED, HIGH);
          
      } else { 

          Serial.print("failed with state "); 

          Serial.print(client.state()); 

          delay(1000); 

      } 

  } 

}

 

void loop() { 
  while(!Serial) {}
  client.loop();
  sensors.requestTemperatures();
  temperatureC = sensors.getTempCByIndex(0);
  Serial.print(temperatureC);
  Serial.println("ºC"); 
  sprintf(tempChar,"%.2f", temperatureC);
  client.publish(topic1, tempChar); //publish temp
  Serial.printf("Published Temp to: %s\n",topic1);
  // Test WDT & Feed
  ESP.wdtFeed();
  delay(5000);
  client.publish(topic2, signal); // publish RSSI
  Serial.printf("Published RSSI to: %s\n",topic2);
  // Test WDT & Feed
  ESP.wdtFeed();
  delay(5000);
  client.publish(topic3, mac); // publish mac address
  Serial.printf("Published mac address to: %s\n",topic3);
  // Test WDT & Feed
  ESP.wdtFeed();
  delay(5000);
//  Serial.println("Going to sleep for 60 seconds");
//  ESP.deepSleep(60e6);
  Serial.println("Going to sleep for 5 minutes");
  ESP.deepSleep(300e6);
}
