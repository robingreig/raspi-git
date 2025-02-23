
char *myStrings[] = {"num1", "num2", "num3"};
int num1 = 47;
int num5 = &num1;

    void setup() {
      Serial.begin(115200);
    }

    void loop() {
      for (byte i = 0; i < 3; i++) {
        Serial.println(myStrings[i]);
        Serial.println("%d\n",num5);
        delay(500);
      }
    }
