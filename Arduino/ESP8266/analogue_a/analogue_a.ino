#define analogPin A0 /* ESP8266 Analog Pin ADC0 = A0 */

int adcValue = 0;  /* Variable to store Output of ADC */

void setup()
{
  Serial.begin(115200); /* Initialize serial communication at 115200 */
}

void loop()
{
  adcValue = analogRead(analogPin); /* Read the Analog Input value */
 
  /* Print the output in the Serial Monitor */
  Serial.print("ADC Value = ");
  Serial.println(adcValue);
  Serial.print("ADC Value corrected for 1.946V = ");
  Serial.println(adcValue-526);
  Serial.print("ADC Value converted to mA = ");
  Serial.println((adcValue-526)/2);
  
  delay(2000);
}
