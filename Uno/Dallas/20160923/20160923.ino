// Include the libraries we need
#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into port 10 on the Arduino
#define ONE_WIRE_BUS 10

char receivedChar;
boolean newData = false;

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);

// arrays to hold device addresses
DeviceAddress insideThermometer, outsideThermometer;

void setup(void)
{
  // start serial port
  Serial.begin(9600);

  // Start up the library
  sensors.begin();

  sensors.getAddress(insideThermometer, 0);
  sensors.getAddress(outsideThermometer, 1);
  if (!sensors.getAddress(insideThermometer, 0)) Serial.println("Unable to find address for Device 0"); 
  if (!sensors.getAddress(outsideThermometer, 1)) Serial.println("Unable to find address for Device 1"); 

  // method 2: search()
  // search() looks for the next device. Returns 1 if a new address has been
  // returned. A zero might mean that the bus is shorted, there are no devices, 
  // or you have already retrieved all of them. It might be a good idea to 
  // check the CRC to make sure you didn't get garbage. The order is 
  // deterministic. You will always get the same devices in the same order
  //
  // Must be called before search()
  oneWire.reset_search();
  // assigns the first address found to insideThermometer
  if (!oneWire.search(insideThermometer)) Serial.println("Unable to find address for insideThermometer");
  // assigns the seconds address found to outsideThermometer
  if (!oneWire.search(outsideThermometer)) Serial.println("Unable to find address for outsideThermometer");

}


// function to print a device address
void printAddress(DeviceAddress deviceAddress)
{
  for (uint8_t i = 0; i < 8; i++)
  {
    // zero pad the address if necessary
    if (deviceAddress[i] < 16) Serial.print("0");
    Serial.print(deviceAddress[i], HEX);
  }
}

// function to print the temperature for a device
void printTemperature(DeviceAddress deviceAddress)
{
  float tempC = sensors.getTempC(deviceAddress);
//  Serial.print("Temp C: ");
  Serial.print(tempC);
//  Serial.print(" Temp F: ");
//  Serial.print(DallasTemperature::toFahrenheit(tempC));
}

// function to print a device's resolution
void printResolution(DeviceAddress deviceAddress)
{
  Serial.print("Resolution: ");
  Serial.print(sensors.getResolution(deviceAddress));
  Serial.println();    
}

// main function to print information about a device
void printData(DeviceAddress deviceAddress)
{
//  Serial.print("Device Address: ");
//  printAddress(deviceAddress);
//  Serial.print(" ");
  printTemperature(deviceAddress);
  Serial.println();
}

// function to look for a new character on the serial input
void recvOneChar() {
  if (Serial.available() > 0){
    receivedChar = Serial.read();
    newData = true;
  }
}

// function to troubleshoot code with debug
void debugCode() {
  Serial.println("Dallas Temperature IC Control Library Demo");
// locate devices on the bus
  Serial.print("Locating devices...");
  Serial.print("Found ");
  Serial.print(sensors.getDeviceCount(), DEC);
  Serial.println(" devices.");
// report parasite power requirements
  Serial.print("Parasite power is: "); 
  if (sensors.isParasitePowerMode()) Serial.println("ON");
  else Serial.println("OFF");
// print device 0 resolution
  Serial.print("Device 0 Resolution: ");
  Serial.print(sensors.getResolution(insideThermometer), DEC); 
  Serial.println();
// print device 1 resolution 
  Serial.print("Device 1 Resolution: ");
  Serial.print(sensors.getResolution(outsideThermometer), DEC); 
  Serial.println();
// show the addresse for device 0
  Serial.print("Device 0 Address: ");
  printAddress(insideThermometer);
  Serial.println();
// show the address for device1
  Serial.print("Device 1 Address: ");
  printAddress(outsideThermometer);
  Serial.println();
  Serial.println();
}  

// function to show new data
void showNewData() {
  if (newData == true) {
//    Serial.print("This just in... ");
//    Serial.println(receivedChar);
    newData = false;
  }
  if (receivedChar == '1') {
//    Serial.println("I received 1");
    printData(insideThermometer);
    Serial.println();
  }else if (receivedChar == '2') {
//    Serial.println("I received 2");
    printData(outsideThermometer);
    Serial.println();
  }else if (receivedChar == '9') {
    debugCode();
  }
  receivedChar = '0';
}

/*
 * Main function, calls the temperatures in a loop.
 */
void loop(void) {

// call sensors.requestTemperatures() to issue a global temperature 
// request to all devices on the bus
// Serial.print("Requesting temperatures...");
  sensors.requestTemperatures();
// Serial.println("DONE");

  recvOneChar();

  showNewData();

  delay (10);
}

