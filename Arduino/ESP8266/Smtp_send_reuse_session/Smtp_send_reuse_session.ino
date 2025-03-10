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

/** Note for library update from v2.x.x to v3.x.x.
 * 
 *  Struct data names changed
 *
 * "ESP_Mail_Session" changes to "Session_Config"
 * "IMAP_Config" changes to "IMAP_Data"
 *
 * Changes in the examples
 *
 * ESP_Mail_Session session;
 * to
 * Session_Config config;
 *
 * IMAP_Config config;
 * to
 * IMAP_Data imap_data;
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

#define WIFI_SSID "Calalta02"
#define WIFI_PASSWORD "Micr0s0ft2018"

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

unsigned long sentMillis = 0;

void setup()
{

    Serial.begin(115200);

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

    Serial.print("Connecting to Wi-Fi");

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
    config.time.ntp_server = F("pool.ntp.org,time.nist.gov");
    config.time.gmt_offset = -7;
    config.time.day_light_offset = 0;
}

void loop()
{
    if (millis() - sentMillis > 3 * 60 * 1000 || sentMillis == 0)
    {
        sentMillis = millis();

        SMTP_Message message;

        message.sender.name = F("ESP Mail");
        message.sender.email = AUTHOR_EMAIL;
        message.subject = F("Send Email with session reusage");
        message.addRecipient(F("user"), RECIPIENT_EMAIL);

        message.html.content = F("<p>This is the HTML message.</p>");
        message.text.content = F("This is the text message");

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
