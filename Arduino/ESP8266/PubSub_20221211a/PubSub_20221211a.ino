#include <ESP8266WiFi.h> 

#include <PubSubClient.h> 

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqtt_broker = "192.168.200.21"; 

const char *topic = "esp8266/mac"; 

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient); 

// initialize mac char variable to send via mqtt
char mac[18];

void setup() { 

  // Set software serial baud to 115200; 

  Serial.begin(115200); 

  // seutp onboard led
  #define LED 2 // onboard led tied to gpio2
  
  pinMode(LED, OUTPUT);

  // connecting to a WiFi network 

  WiFi.begin(ssid, password); 

  while (WiFi.status() != WL_CONNECTED) { 

      delay(500); 

      Serial.println("Connecting to WiFi.."); 

  } 

  Serial.println("Connected to the WiFi network"); 
  // turn on onboard led
  digitalWrite(LED, HIGH);

  //connecting to a mqtt broker 

  client.setServer(mqtt_broker, mqtt_port); 

  client.setCallback(callback); 

  while (!client.connected()) { 

      String client_id = "esp8266 > "; 

      client_id += String(WiFi.macAddress());

      Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 

      if (client.connect(client_id.c_str())) { 

          Serial.println("Mqtt broker connected"); 
          digitalWrite(LED, HIGH);
          
      } else { 

          Serial.print("failed with state "); 

          Serial.print(client.state()); 

          delay(2000); 

      } 

  } 

  // publish and subscribe

  String macStr = String(WiFi.macAddress());

  strcpy(mac, macStr.c_str());

  client.publish(topic, mac); 

  client.subscribe(topic); 

} 

 

void callback(char *topic, byte *payload, unsigned int length) { 

  Serial.print("Message arrived in topic: "); 

  Serial.println(topic); 

  Serial.print("Message:"); 

  for (int i = 0; i < length; i++) { 

      Serial.print((char) payload[i]); 

  } 

  Serial.println(); 

  Serial.println("-----------------------"); 

} 

 

void loop() { 

  client.loop(); 

} 
