const int pinoSensor = 4; 

void setup() {
    Serial.begin(9600); 
    pinMode (pinoSensor, INPUT); 
}

void loop() {

    if(digitalRead(pinoSensor) == HIGH){ 
        Serial.println("Iluminado");
    }
    else{ 
       Serial.println("Aus�ncia de luz"); 
    }

}
