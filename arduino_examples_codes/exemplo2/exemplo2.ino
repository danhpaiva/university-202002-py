const int pinLED = 9;

void setup() {
   pinMode(pinLED, OUTPUT); 
   Serial.begin(9600);
}

 void loop() {
    // primeiro o LED vai brilhar cada vez mais
    for(int i=0; i<256; i++) {
       analogWrite(pinLED, i);
       delay(5);
       Serial.println(i);
    }

    // depois o LED vai esmaecendo
    for(int i=255; i>=0; i--) {
       analogWrite(pinLED, i);
       delay(5);
       Serial.println(i);
    }  

    delay(1000);
}
