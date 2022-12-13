#include <ESP8266WiFi.h> 

#include <PubSubClient.h> 

// WiFi 

//const char *ssid = "Calalta02"; // Enter your WiFi name 

//const char *password = "Micr0s0ft2018";  // Enter WiFi password 

const char *ssid = "MakerSpaceTest"; // Enter your WiFi name 

const char *password = "P@55w0rd";  // Enter WiFi password 

// MQTT Broker 

//const char *mqtt_broker = "192.168.200.21"; 

const char *mqtt_broker = "192.168.204.1"; 

const char *topic1 = "esp8266/test";

const char *topic2 = "esp8266/reply";

const char *mqtt_username = "emqx"; 

const char *mqtt_password = "public"; 

const int mqtt_port = 1883; 

WiFiClient espClient; 

PubSubClient client(espClient);

void setup() { 

  // Set software serial baud to 115200; 

  Serial.begin(115200); 

  // seutp onboard led
  #define LED 2 // onboard led tied to gpio2
  #define Green 15 // Green led tied to gpio8
  
  pinMode(LED, OUTPUT);
  pinMode(Green, OUTPUT);

  // connecting to a WiFi network 

  WiFi.begin(ssid, password); 

  while (WiFi.status() != WL_CONNECTED) { 

      delay(500); 

      Serial.println("Connecting to WiFi.."); 

  } 

  Serial.println("Connected to the WiFi network"); 
  // turn on onboard led
//  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(LED, HIGH);

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
          digitalWrite(Green, HIGH);
          
      } else { 

          Serial.print("failed with state "); 

          Serial.print(client.state()); 

          delay(2000); 

      } 

  } 

  // publish and subscribe  

  client.subscribe(topic1); 

} 

 

void callback(char *topic1, byte *payload, unsigned int length) { 

  Serial.print("Message arrived in topic1: "); 

  Serial.println(topic1); 

  Serial.print("Message:");
  Serial.println((char)payload[0]);
  int a = ((char) payload[0]); // store ascii of payload into a
  Serial.print("ascii of payload[0] = ");
  Serial.println(a);
  int b = a - '0';
  Serial.print("a - '0' = ");
  Serial.println(b);
  switch (b)
  {
    case (0):
      Serial.println("Received a 0 and publishing");
      client.publish(topic2, "Received a 0");
      break;
    case (1):
      Serial.println("Received a 1 and publishing");
      client.publish(topic2, "Received a 1");
      break;
    default:
      Serial.println("Default response from case statement");
      break;
  }

  Serial.println(); 

  Serial.println("-----------------------");
  
} 

 

void loop() { 

  client.loop(); 

} 
