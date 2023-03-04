

void setup() {
 
  Serial.begin(115200);
}
  
void loop()
{
  
  // Read the Analogue Input value
  adcValue = analogRead(analogPin);
  // Print the output in the Serial Monitor
  Serial.print("ADC Value = ");
  Serial.println(adcValue);
  // Convert the adcValue int to a string
  adcString=String(adcValue);
  Serial.print("ADC String = ");
  Serial.println(adcString);
  // Convert the adcString to a char
  adcString.toCharArray(adcChar,5);
  Serial.print("ADC Char = ");
  Serial.println(adcChar);
  // delay 5 seconds (5 x 1000 = 5000)
  delay(5000);
}
