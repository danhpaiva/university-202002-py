const int pinSensor = A1;
int valor;

void setup() {
    Serial.begin(9600);
    delay(1000);
}

void loop() {
    valor =  analogRead(pinSensor);
    Serial.println(valor);
    delay(1000);
}
