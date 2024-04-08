#define analogPin A0 /* ESP8266 Analog Pin ADC0 = A0 */

int adcSample = 0; // Variable to store sample ADC

int adcValue = 0; // Variable to store running total of ADC samples

int adcAverage = 0; // Variable to average value of ADC

float adcFloat = 0; //Variable to convert ADC value to battery voltag

char adcFloatChar[6]; // Variable to store battery voltage as a char

void setup()
{
  Serial.begin(115200); /* Initialize serial communication at 115200 */
}

void loop()
{
  adcValue = analogRead(analogPin); /* Read the Analog Input value */
 
  // Sample the battery voltage x 3 then publish
//  adcValue = 0; // Reset adcValue to 0  
  for (int i = 1; i < 4; i++) {
    // Read the Analogue Input value
    adcSample = analogRead(analogPin);
    // Print the output in the Serial Monitor
    Serial.print("ADC Sample = ");
    Serial.println(adcSample);
    adcValue += adcSample;
    Serial.print("ADC Value = ");
    Serial.println(adcValue);
    adcAverage = (adcValue/i);
    Serial.print("ADC Average = ");
    Serial.println(adcAverage);
  }
    /* Convert the digital ADC value to the actual voltage 
     *  as a float using a 12K and 3K3 resistor*/
//  adcFloat = adcAverage * 0.0142;
  adcFloat = adcAverage * 0.01465; // reads 15.0vdc @ 3.3vdc input
  Serial.print("ADC Float = ");
  Serial.println(adcFloat);
  // Convert voltage float into char
  sprintf(adcFloatChar, "%.2f", adcFloat);
  Serial.print("ADC Float Char = ");
  Serial.println(adcFloatChar);
  Serial.println();
  Serial.println();
  delay(10000);
}
