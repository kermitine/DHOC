/*
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the DHOC project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
*/

const int ledPin = 12; // pin which led is connected to

void setup() {
  pinMode(ledPin, OUTPUT); // Set the LED pin as an output
  Serial.begin(9600);     // Initialize serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available()) { // Check if there's incoming data in the serial buffer
    char command = Serial.read(); // Read the incoming character and store as a string character

    if (command == '1') { // If '1' is received, turn LED on
      digitalWrite(ledPin, HIGH);
      Serial.println("LED ON"); // Send 'on' confirmation back to serial monitor
    } else if (command == '0') { // If '0' is received, turn LED off
      digitalWrite(ledPin, LOW);
      Serial.println("LED OFF"); // Send 'off' confirmation back to Python
    }
  }
}