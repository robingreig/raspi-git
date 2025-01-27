/**
 * Created by K. Suwatchai (Mobizt)
 *
 * Email: suwatchai@outlook.com
 *
 * Github: https://github.com/mobizt/ESP-Mail-Client
 *
 * Copyright (c) 2023 mobizt
*/

// This example show how to login once for sending multiple messages.

/*  RobinGreig
 *  2025.01.26
 *  Smtp_send_reuse_session_20250126b
 *  sending every 2 minutes
 *  Using timezone
 *  config.time.timezone_env_string = "MST7MDT,M3.2.0,M11.1.0"; //Denver
 *  
 *  Smtp_send_reuse_session_20250126c
 *  Sending text instead of html
 *  
 *  Smtp_send_reuse_session_20250126d
 *  Sending ds18b20 temp
 *  
 *  Smtp_send_reuse_session_20250126e
 *  Setup digital input 
 *  Send an email at start
 *  Send an email when input first goes high
 *  Send an email every 5 minutes (interval) if input stays high 
 *  
 *  Smtp_send_reuse_session_20250126e
 *  Add temperature monitoring
 *  Send email if temp < 15C
 *  
 *  Smtp_send_reuse_session_20250126g
 *  Add SAIT hotspot
 *  
 *  Smtp_ds18b20_button_20250127a
 *  Trying to connect moisture sensor to ESP8266  
 *  No Water - LED Off - Digital Output HIGH
 *  Water - LED On - Digital Output LOW
 *  
 */

#include <Arduino.h>
#if defined(ESP32) || defined(ARDUINO_RASPBERRY_PI_PICO_W)
#include <WiFi.h>
#elif defined(ESP8266)
#include <ESP8266WiFi.h>
#elif __has_include(<WiFiNINA.h>)
#include <WiFiNINA.h>
#elif __has_include(<WiFi101.h>)
#include <WiFi101.h>
#elif __has_include(<WiFiS3.h>)
#include <WiFiS3.h>
#endif

#include <ESP_Mail_Client.h>
#include <OneWire.h>
#include <DallasTemperature.h>

//#define WIFI_SSID "Calalta02"
//#define WIFI_PASSWORD "Micr0s0ft2018"
#define WIFI_SSID "Raspi32"
#define WIFI_PASSWORD "P@55w0rd2025"
// If sensor goes high how long is the delay between emails?
int interval = 5; // in minutes
// Low Temperature Threshold
int lowTemp = 15;

/** For Gmail, the app password will be used for log in
 *  Check out https://github.com/mobizt/ESP-Mail-Client#gmail-smtp-and-imap-required-app-passwords-to-sign-in
 *
 * For Yahoo mail, log in to your yahoo mail in web browser and generate app password by go to
 * https://login.yahoo.com/account/security/app-passwords/add/confirm?src=noSrc
 *
 * To use Gmai and Yahoo's App Password to sign in, define the AUTHOR_PASSWORD with your App Password
 * and AUTHOR_EMAIL with your account email.
 */

/** The smtp host name e.g. smtp.gmail.com for GMail or smtp.office365.com for Outlook or smtp.mail.yahoo.com */
#define SMTP_HOST "smtp.gmail.com"

/** The smtp port e.g.
 * 25  or esp_mail_smtp_port_25
 * 465 or esp_mail_smtp_port_465
 * 587 or esp_mail_smtp_port_587
 */
//#define SMTP_PORT esp_mail_smtp_port_587
#define SMTP_PORT esp_mail_smtp_port_465

/* The log in credentials */
#define AUTHOR_EMAIL "canukalert@gmail.com"
#define AUTHOR_PASSWORD "ghjb zvxz jhvw znzr"

/* Recipient email address */
#define RECIPIENT_EMAIL "robin.greig@calalta.com"

SMTPSession smtp;

Session_Config config;

void smtpCallback(SMTP_Status status);

#if defined(ARDUINO_RASPBERRY_PI_PICO_W)
WiFiMulti multi;
#endif

#include "HeapStat.h"
HeapStat heapInfo;

// Setup sentMillis for delay calculation
unsigned long sentMillis = 0;

// ESP8266 number 18
int num = 18;

// toggle variable to decide if we send an email
int toggle = 0;

// GPIO where the DS18B20 is connected to GPIO14 (D5)
const int oneWireBus = 14;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

// Setup float variable to hold temperature reading
float temperatureC;

void setup()
{
    Serial.begin(115200);

    // Start the DS18B20 sensor
    sensors.begin();

    // Setup input digital pin to go HIGH when water detected
//    pinMode(12, INPUT);
    // Setup input digital pin to go HIGH when water detected
    pinMode(12, INPUT_PULLUP);

#if defined(ARDUINO_ARCH_SAMD)
    while (!Serial)
        ;
#endif

    Serial.println();

#if defined(ARDUINO_RASPBERRY_PI_PICO_W)
    multi.addAP(WIFI_SSID, WIFI_PASSWORD);
    multi.run();
#else
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
#endif
    Serial.println();
    Serial.println("Connecting to Wi-Fi");

#if defined(ARDUINO_RASPBERRY_PI_PICO_W)
    unsigned long ms = millis();
#endif

    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(300);
#if defined(ARDUINO_RASPBERRY_PI_PICO_W)
        if (millis() - ms > 10000)
            break;
#endif
    }
    Serial.println();
    Serial.print("Connected with IP: ");
    Serial.println(WiFi.localIP());
    Serial.println();

    MailClient.networkReconnect(true);

#if defined(ARDUINO_RASPBERRY_PI_PICO_W)
    MailClient.clearAP();
    MailClient.addAP(WIFI_SSID, WIFI_PASSWORD);
#endif

    smtp.debug(1);

    smtp.callback(smtpCallback);

    config.server.host_name = SMTP_HOST;
    config.server.port = SMTP_PORT;
    config.login.email = AUTHOR_EMAIL;
    config.login.password = AUTHOR_PASSWORD;

    config.login.user_domain = F("127.0.0.1");

    /*
    Set the NTP config time
    For times east of the Prime Meridian use 0-12
    For times west of the Prime Meridian add 12 to the offset.
    Ex. American/Denver GMT would be -6. 6 + 12 = 18
    See https://en.wikipedia.org/wiki/Time_zone for a list of the GMT/UTC timezone offsets
    */
    config.time.ntp_server = F("time1.sait.ca,pool.ntp.org,time.nist.gov");
    config.time.gmt_offset = 0;
    config.time.day_light_offset = 0;
    config.time.timezone_env_string = "MST7MDT,M3.2.0,M11.1.0"; //Denver
    //https://github.com/nayarsystems/posix_tz_db/blob/master/zones.csv
}

void loop()
{
    int sensorVal = digitalRead(12);
    Serial.print("sensorVal: ");
    Serial.println(sensorVal);
    sensors.requestTemperatures(); 
    temperatureC = sensors.getTempCByIndex(0);
    Serial.println();
    Serial.print("Temperature: ");
    Serial.print(temperatureC);
    Serial.println("ºC");
    // send email at start
    if (sentMillis == 0){
      toggle = 1;
      sentMillis = 1;
      Serial.println("sentMillis == 0");
      Serial.print("Interval = ");
      Serial.println(interval);
    // send email if sensor goes high or lowTemp the first time
    } else if ((sensorVal == LOW || temperatureC < lowTemp) && sentMillis == 1) { 
      toggle = 1;
      Serial.println("sensorVal == LOW && sentMillis == 1");
      sentMillis = millis();
//    } else if (sensorVal == LOW && millis() - sentMillis > 2 * 60 * 1000) {
    // send email every interval if sensor stays high or temp stays low
    } else if ((sensorVal == LOW || temperatureC < lowTemp) && millis() - sentMillis > interval * 60 * 1000) {
      toggle = 1;
      sentMillis = millis();
      Serial.println("sensorVal == LOW && millis() - sentMillis > 2*60*1000");
    } else {
      toggle = 0;
    }
    
//    if (millis() - sentMillis > 2 * 60 * 1000 || sentMillis == 0)
    if (toggle > 0)
    {
        toggle = 0;
//        sentMillis = millis();

//        sensors.requestTemperatures(); 
//        temperatureC = sensors.getTempCByIndex(0);
//        Serial.println();
//        Serial.print("Temperature: ");
//        Serial.print(temperatureC);
//        Serial.println("ºC");

        SMTP_Message message;

        message.sender.name = F("ESP Mail");
        message.sender.email = AUTHOR_EMAIL;
        // Send first email subject "First Email at Startup"
        if (sentMillis == 1) {
          message.subject = F("First Email at Startup");
        }
        if (sensorVal < 1) {
          message.subject = F("Water Leak Detected !!");
        }
        if (temperatureC <= lowTemp) {
          message.subject = F("Low Temperature Detected !!");
        }
        
        message.addRecipient(F("user"), RECIPIENT_EMAIL);

        //message.html.content = F("<p>This is the HTML message.</p>");
        //message.text.content = F("This is the text message");

        //Send raw text message
        String textMsg = "Sent from ESP8266-"+String(num)+String("\n");
        textMsg += "IP Address is: "+String(WiFi.localIP().toString())+String("\n");
        textMsg += "RSSI is: "+String(WiFi.RSSI())+String("\n");
        textMsg += "MAC Address is: "+String(WiFi.macAddress())+String("\n"); 
        textMsg += String("\n");
        if (sensorVal < 1){
          textMsg += "****** Water WAS detected ******"+String("\n");
        } else {
          textMsg += "Water was NOT detected"+String("\n");
        }
        textMsg += String("\n");
        textMsg += "Temperature: "+String(temperatureC)+String("\n");
        textMsg += String("\n");
        if (temperatureC <= lowTemp){
          textMsg += "****** Low Temperature WAS detected ******"+String("\n");
        } else {
          textMsg += "Low Temperature was NOT detected"+String("\n");
        }
        textMsg += String("\n");
        message.text.content = textMsg.c_str();
        message.text.charSet = "us-ascii";
        message.text.transfer_encoding = Content_Transfer_Encoding::enc_7bit;
  
        message.priority = esp_mail_smtp_priority::esp_mail_smtp_priority_low;
        message.response.notify = esp_mail_smtp_notify_success | esp_mail_smtp_notify_failure | esp_mail_smtp_notify_delay;


        Serial.println();
        Serial.println("Sending Email...");

        if (!smtp.isLoggedIn())
        {
            /* Set the TCP response read timeout in seconds */
            // smtp.setTCPTimeout(10);

            if (!smtp.connect(&config))
            {
                MailClient.printf("Connection error, Status Code: %d, Error Code: %d, Reason: %s\n", smtp.statusCode(), smtp.errorCode(), smtp.errorReason().c_str());
                goto exit;
            }

            if (!smtp.isLoggedIn())
            {
                Serial.println("Error, Not yet logged in.");
                goto exit;
            }
            else
            {
                if (smtp.isAuthenticated())
                    Serial.println("Successfully logged in.");
                else
                    Serial.println("Connected with no Auth.");
            }
        }

        if (!MailClient.sendMail(&smtp, &message, false))
            MailClient.printf("Error, Status Code: %d, Error Code: %d, Reason: %s\n", smtp.statusCode(), smtp.errorCode(), smtp.errorReason().c_str());

    exit:

        heapInfo.collect();
        heapInfo.print();
    }
    delay(500);
}

/* Callback function to get the Email sending status */
void smtpCallback(SMTP_Status status)
{

    Serial.println(status.info());

    if (status.success())
    {

        Serial.println("----------------");
        MailClient.printf("Message sent success: %d\n", status.completedCount());
        MailClient.printf("Message sent failed: %d\n", status.failedCount());
        Serial.println("----------------\n");

        for (size_t i = 0; i < smtp.sendingResult.size(); i++)
        {
            SMTP_Result result = smtp.sendingResult.getItem(i);

            MailClient.printf("Message No: %d\n", i + 1);
            MailClient.printf("Status: %s\n", result.completed ? "success" : "failed");
            MailClient.printf("Date/Time: %s\n", MailClient.Time.getDateTimeString(result.timestamp, "%B %d, %Y %H:%M:%S").c_str());
            MailClient.printf("Recipient: %s\n", result.recipients.c_str());
            MailClient.printf("Subject: %s\n", result.subject.c_str());
        }
        Serial.println("----------------\n");

        smtp.sendingResult.clear();
    }
}
