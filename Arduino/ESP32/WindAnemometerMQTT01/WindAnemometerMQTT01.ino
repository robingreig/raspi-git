/*********
 * Filename: WindAnemometerMQTT01
 * for ESP32
 * Robin Greig
 * 2025.01.31
 * Receives RS-485 data from wind direction module and sends it via mqtt
 * to Mosquitto broker mqtt43, 192.168.200.143
 * 
 * 
 * based on the esp32 mqtt file from:
 * Rui Santos
 * Complete project details at https://randomnerdtutorials.com  
 * 
 * ##### 
 * Has an error compiling for ESP32 Dev Module
 * Compiles the first time then errors out
 * Have to restart the Arduino IDE and the will compile again
 * #####
*********/

#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <HardwareSerial.h>
 
// Create a HardwareSerial object to communicate with the MAX485 module
HardwareSerial mySerial(2); // Using UART2 (TX2, RX2)
 
// Define Modbus parameters
const byte slaveAddress = 0x01;          // Address of the Modbus slave device
const byte functionCode = 0x03;          // Function code to read holding registers
const byte startAddressHigh = 0x00;      // High byte of the starting address
const byte startAddressLow = 0x00;       // Low byte of the starting address
const byte registerCountHigh = 0x00;     // High byte of the number of registers to read
const byte registerCountLow = 0x02;      // Low byte of the number of registers to read

// Replace the next variables with your SSID/Password combination
const char* ssid = "Calalta02";
const char* password = "Micr0s0ft2018";

// Add your MQTT Broker IP address, example:
//const char* mqtt_server = "192.168.1.144";
const char* mqtt_server = "192.168.200.143";

WiFiClient espClient;
PubSubClient client(espClient);

// setup speeds global variable for mqtt
int speed11;

// setup rssi global variable for mqtt
char rssiSignal[6];

// last message sent time
long lastMsg = 0;

char msg[50];

int value = 0;

void setup() {
  // Initialize serial communications for debugging
  Serial.begin(115200);
  
  // Initialize HardwareSerial for Modbus communication
  mySerial.begin(4800, SERIAL_8N1, 16, 17); // RX2=16, TX2=17 for UART2
 
  // Allow some time for initialization
  delay(500);
  
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

}

void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println();
  
}

void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();

  // Feel free to add more if statements to control more GPIOs with MQTT

  // If a message is received on the topic esp32/output, you check if the message is either "on" or "off". 
  // Changes the output state according to the message
  if (String(topic) == "esp32/output") {
    Serial.print("Changing output to ");
    if(messageTemp == "on"){
      Serial.println("on");
    }
    else if(messageTemp == "off"){
      Serial.println("off");
    }
  }
}

void reconnectMQTT() {
  // Loop until we're reconnected
  while (!client.connected()) {
    // Attempt to connect
    Serial.print("Attempting MQTT connection...");
    // Establish unique ID string
    String client_id = "esp32 > ";
    client_id += String(WiFi.macAddress());
    Serial.printf("The client %s is connecting to the mqtt broker\n", client_id.c_str()); 
//      if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) { 
    if (client.connect(client_id.c_str())) {
      Serial.println("connected");
      String WiFiRSSI = String(WiFi.RSSI());
      Serial.printf("The client RSSI is %s\n",WiFiRSSI.c_str());
      strcpy(rssiSignal, WiFiRSSI.c_str()); 
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void loop() {

  // Connect to WiFi
  if (!client.connected()) {
    reconnectMQTT();
  }
  client.loop();
  
  // Create a request frame for Modbus communication
  byte requestFrame[8];
  constructModbusRequest(requestFrame, slaveAddress, functionCode, startAddressHigh, startAddressLow, registerCountHigh, registerCountLow);
 
  // Send the Modbus request frame
  sendModbusRequest(requestFrame, 8);
 
  // Read and process the Modbus response frame
  if (mySerial.available()) {
    // Create a buffer to store the response frame
    byte responseFrame[9];
    // Read the response frame from the slave device
    readModbusResponse(responseFrame, 9);
    // Verify the CRC of the received response frame
    if (verifyCRC(responseFrame, 9)) {
      // Process the response frame to extract data
      processModbusResponse(responseFrame);
    } else {
      // Print an error message if CRC verification fails
      Serial.println("CRC error.");
    }
  } else {
    // Print an error message if no response is received
    Serial.println("No response from slave.");
  }

  long now = millis();
  if (now - lastMsg > 1000) {
    lastMsg = now;
    
    // Convert the speed value to a char array
    // Convert voltage float into char
    char tempString1[8];
    dtostrf(speed11, 1, 0, tempString1);
    Serial.print("Speed to be sent via MQTT: ");
    Serial.println(tempString1);
    client.publish("esp32/00/speed", tempString1);
    Serial.println();
    
//    // Convert the degree value to a char array
//    char tempString2[4];
//    dtostrf(degrees, 1, 0, tempString2);
//    Serial.print("Degrees to be sent via mqtt: ");
//    Serial.println(tempString2);
//    client.publish("esp32/01/degree", tempString2);
  }
 
  // Wait for 1 second before the next request
  delay(1000);
}
 
// Function to construct a Modbus request frame
void constructModbusRequest(byte *frame, byte address, byte function, byte startHigh, byte startLow, byte countHigh, byte countLow) {
  frame[0] = address;          // Address of the slave device
  frame[1] = function;         // Function code
  frame[2] = startHigh;        // High byte of the starting address
  frame[3] = startLow;         // Low byte of the starting address
  frame[4] = countHigh;        // High byte of the number of registers to read
  frame[5] = countLow;         // Low byte of the number of registers to read
 
  // Calculate and append the CRC to the request frame
  uint16_t crc = calculateCRC(frame, 6);
  frame[6] = crc & 0xFF;         // CRC low byte
  frame[7] = (crc >> 8) & 0xFF;  // CRC high byte
}
 
// Function to send a Modbus request frame
void sendModbusRequest(byte *frame, byte length) {
  for (byte i = 0; i < length; i++) {
    mySerial.write(frame[i]); // Send each byte of the frame
  }
}
 
// Function to read a Modbus response frame
void readModbusResponse(byte *frame, byte length) {
  for (byte i = 0; i < length; i++) {
    if (mySerial.available()) {
      frame[i] = mySerial.read(); // Read each byte of the frame
    }
  }
}
 
// Function to verify the CRC of a Modbus frame
bool verifyCRC(byte *frame, byte length) {
  uint16_t receivedCRC = (frame[length - 1] << 8) | frame[length - 2]; // Extract the received CRC
  // Calculate the CRC of the received frame (excluding the received CRC bytes)
  return calculateCRC(frame, length - 2) == receivedCRC;
}
 
// Function to process the Modbus response frame and extract data
void processModbusResponse(byte *frame) {
  // Extract the speed data from the response frame
  uint16_t speed1 = (frame[3] << 8) | frame[4];
  uint16_t speed2 = (frame[5] << 8) | frame[6];

  // Print the cardinal and degree values to the Serial Monitor
  Serial.print("Speed1: ");
  Serial.print(speed1);
  speed11 = speed1;
  Serial.println();
  
  Serial.print("Speed2: ");
  Serial.print(speed2);
  Serial.println();
  
}
 
// Function to calculate the CRC of a Modbus frame
uint16_t calculateCRC(byte *frame, byte length) {
  uint16_t crc = 0xFFFF; // Initialize CRC to 0xFFFF
  for (byte i = 0; i < length; i++) {
    crc ^= frame[i]; // XOR the frame byte with the CRC
    for (byte j = 0; j < 8; j++) {
      if (crc & 0x0001) { // Check if the LSB of the CRC is 1
        crc >>= 1;        // Right shift the CRC
        crc ^= 0xA001;    // XOR the CRC with the polynomial 0xA001
      } else {
        crc >>= 1;        // Right shift the CRC
      }
    }
  }
  return crc; // Return the calculated CRC
}
