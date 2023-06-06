/*The following code's object is to receive OSC messages 
of stored data, to be used to fulfill the conditional statements 
in order to simulate movement imagery.*/

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <OSCMessage.h>
#include <OSCBundle.h>
#include <OSCData.h>

const char* ssid = "Dherman";          // your network SSID (name)
const char* pass = "Kevind555!";       // your network password

// A UDP instance to let us send and receive packets over UDP
WiFiUDP Udp;

// this is the port that our computer is sending the data to
const unsigned int localPort = 8888;       

//protocol to represent error codes
OSCErrorCode error;

void setup() {

  //Pin Declaration
  pinMode(14, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(15, OUTPUT);

  //Boot up 115200 BAUD
  Serial.begin(115200);
  
  Serial.println();
  Serial.println();

  Serial.print("Connecting to ");
  Serial.println(ssid);
  Serial.print("...");

  // Connect to WiFi network
  WiFi.begin(ssid, pass);

  //wait until connected
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  //Once connected:
  Serial.println("");

  //print network name and details
  // turn on blue LED to indicate wifi is conneected
  digitalWrite(15, HIGH);
  Serial.println("WiFi CONNECTED to: ");
  Serial.println(ssid);
  Serial.println(" ");

  //print Ip address
  Serial.println("IP address of NodeMCU: ");
  Serial.println(WiFi.localIP());
  Serial.println(" ");

  //initialize a UDP connection and attach port to recives data packets
  Serial.println("Starting UDP...");
  Udp.begin(localPort);
  Serial.print("Local port: ");
  Serial.println(Udp.localPort());
  Serial.print("Ready");  
  Serial.print(" "); 
}

//This function is triggered when we recieve a message    
void led(OSCMessage &msg) {

  /*This code block the message if the first index is a float
  and if it a flaot it will be store. Then if the store value 
  meets the conditions statement, the red led wil turn on.*/
  if (msg.isFloat(0)) {
    float right = msg.getFloat(0); 
    if(right > 0.69){
      digitalWrite(14, HIGH); 
    }
    else{
      digitalWrite(14, LOW);
    }
  }
  /*This code block the second message if the first index is 
  a float and if it a flaot it will be store. Then if the store 
  value meets the conditions statement, the green led wil turn on.*/
  if (msg.isFloat(1)) {
    float left_prediction = msg.getFloat(1);
    if (left_prediction > 0.31){
      digitalWrite(12, HIGH); 
    }
    else{
      digitalWrite(12, LOW);
    }
  }
}


void loop() {

  //protocol used for representing OSC messages
  OSCMessage msg;
  
  //stores the size of the UDP packet that was received, or zero if no packet was received
  int size = Udp.parsePacket();

  //condition statement if there is actually a msg.
  if (size > 0) {
    //In this code loop, the message is read byte by byte as size decrements 
    //and then appends to a message
    while (size--) {
      msg.fill(Udp.read());
    }
    
    //Used to check whether an OSC message has any errors
    if (!msg.hasError()) {

      //If the OSC doesnt have this address the NodeMCU wont recieve anything
      msg.dispatch("/data", led);
    } 

    //Print error to debug
    else {
      error = msg.getError();
      Serial.print("error: ");
      Serial.println(error);
    }
  }
}



