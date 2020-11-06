#include "Ultrasonic.h"

Ultrasonic ultrasonic(7, 6);

void setup() {
    Serial.begin(9600);
}

void loop() {
    Serial.println(ultrasonic.Ranging(CM));
    Serial.println("cm");
    delay(1000);
}
