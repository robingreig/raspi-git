#include <ESP8266WiFi.h> 

#include <PubSubClient.h> 

// WiFi 

const char *ssid = "Calalta02"; // Enter your WiFi name 

const char *password = "Micr0s0ft2018";  // Enter WiFi password 

// MQTT Broker 

const char *mqtt_broker = "192.168.200.21"; 

const char *topic = "esp8266/test"; 

const char *mqtt_username = "emqx"; 

const char *mqtt_password = "public"; 

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient); 

 

void setup() { 
  // Set pin 14 as output
  pinMode(14, OUTPUT);
  digitalWrite(14, LOW);

  // Set software serial baud to 115200; 

  Serial.begin(115200); 

  // connecting to a WiFi network 

  WiFi.begin(ssid, password); 

  while (WiFi.status() != WL_CONNECTED) { 

      delay(500); 

      Serial.println("Connecting to WiFi.."); 

  } 

  Serial.println("Connected to the WiFi network"); 

  //connecting to a mqtt broker 

  client.setServer(mqtt_broker, mqtt_port); 

  client.setCallback(callback); 

  while (!client.connected()) { 

      String client_id = "esp8266-00 > "; 

      client_id += String(WiFi.macAddress());

      Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 

//      if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) { 
      if (client.connect(client_id.c_str())) { 

          Serial.println("Mqtt broker connected"); 

      } else { 

          Serial.print("failed with state "); 

          Serial.print(client.state()); 

          delay(2000); 

      } 

  } 

  // publish and subscribe 

  client.publish(topic, "hello emqx"); 

  client.subscribe(topic); 

} 

 

void callback(char *topic, byte *payload, unsigned int length) { 

  Serial.print("Message arrived in topic: "); 

  Serial.println(topic); 

  Serial.print("Message:"); 

  for (int i = 0; i < length; i++) { 

      Serial.print((char) payload[i]); 

  } 

  digitalWrite(14, HIGH);
  delay(2000);
  digitalWrite(14, LOW);
  
  Serial.println(); 

  Serial.println("-----------------------"); 

} 

 

void loop() { 

  client.loop(); 

} 
