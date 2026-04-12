/* influxdb20260411b
 *  11 April 2026
 *  Robin Greig
 *  Connecting to the Influxdb on mqtt43
 *  And uploading RSSI data to RainGauge bucket
 *  
*/




#if defined(ESP32)
  #include <WiFiMulti.h>
  WiFiMulti wifiMulti;
  #define DEVICE "ESP32"
  #elif defined(ESP8266)
  #include <ESP8266WiFiMulti.h>
  ESP8266WiFiMulti wifiMulti;
  #define DEVICE "ESP8266"
  #endif
  
  #include <InfluxDbClient.h>
  #include <InfluxDbCloud.h>
  
  // WiFi AP SSID
  #define WIFI_SSID "Calalta02"
  // WiFi password
  #define WIFI_PASSWORD "Micr0s0ft2018"
  
  #define INFLUXDB_URL "http://192.168.200.43:8086"
  #define INFLUXDB_TOKEN "H95pyxmWChi6dJQd4RGhCxHPUSCrn67NZCx4uRlIbNZaYIdRA8MQMByYQxXlWzDeCymvYG4YdyrYEYkGZVv97w=="
  #define INFLUXDB_ORG "7512cf9b48f5285e"
  #define INFLUXDB_BUCKET "RainGauge"
  
  // Time zone info
  #define TZ_INFO "UTC-6"
  
  // Declare InfluxDB client instance with preconfigured InfluxCloud certificate
  InfluxDBClient client(INFLUXDB_URL, INFLUXDB_ORG, INFLUXDB_BUCKET, INFLUXDB_TOKEN, InfluxDbCloud2CACert);
  
  // Declare Data point
  Point sensor("wifi_status");
  
  void setup() {
    Serial.begin(115200);
  
    // Setup wifi
    WiFi.mode(WIFI_STA);
    wifiMulti.addAP(WIFI_SSID, WIFI_PASSWORD);
  
    Serial.print("Connecting to wifi");
    while (wifiMulti.run() != WL_CONNECTED) {
      Serial.print(".");
      delay(100);
    }
    Serial.println();
  
    // Accurate time is necessary for certificate validation and writing in batches
    // We use the NTP servers in your area as provided by: https://www.pool.ntp.org/zone/
    // Syncing progress and the time will be printed to Serial.
    timeSync(TZ_INFO, "pool.ntp.org", "time.nis.gov");
  
  
    // Check server connection
    if (client.validateConnection()) {
      Serial.print("Connected to InfluxDB: ");
      Serial.println(client.getServerUrl());
    } else {
      Serial.print("InfluxDB connection failed: ");
      Serial.println(client.getLastErrorMessage());
    }
        // Add tags to the data point
    sensor.addTag("device", DEVICE);
    sensor.addTag("SSID", WiFi.SSID());
  }
  void loop() {
    // Clear fields for reusing the point. Tags will remain the same as set above.
    sensor.clearFields();
  
    // Store measured value into point
    // Report RSSI of currently connected network
    sensor.addField("rssi", WiFi.RSSI());
  
    // Print what are we exactly writing
    Serial.print("Writing: ");
    Serial.println(sensor.toLineProtocol());
  
    // Check WiFi connection and reconnect if needed
    if (wifiMulti.run() != WL_CONNECTED) {
      Serial.println("Wifi connection lost");
    }
  
    // Write point
    if (!client.writePoint(sensor)) {
      Serial.print("InfluxDB write failed: ");
      Serial.println(client.getLastErrorMessage());
    }
  
    Serial.println("Waiting 30 seconds");
    delay(30000);
    }
