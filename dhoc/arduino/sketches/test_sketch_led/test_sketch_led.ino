const int ledPin = 12; // Using the built-in LED on pin 12

void setup() {
  pinMode(ledPin, OUTPUT); // Set the LED pin as an output
  Serial.begin(9600);     // Initialize serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available()) { // Check if there's incoming serial data
    char command = Serial.read(); // Read the incoming character

    if (command == '1') { // If '1' is received, turn LED on
      digitalWrite(ledPin, HIGH);
      Serial.println("LED ON"); // Send confirmation back to Python
    } else if (command == '0') { // If '0' is received, turn LED off
      digitalWrite(ledPin, LOW);
      Serial.println("LED OFF"); // Send confirmation back to Python
    }
  }
}