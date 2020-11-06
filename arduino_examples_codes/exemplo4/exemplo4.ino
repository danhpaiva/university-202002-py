#include <dht11.h>

#define DHT11PIN 2
dht11 DHT11;

void setup()  {
    Serial.begin(9600);
    delay(1000);
}
 
void loop()  {
    DHT11.read(DHT11PIN);
    Serial.println("1) Umidade: ");
    Serial.println(DHT11.humidity);
    Serial.println(" % ");
    Serial.println("2) Temperatura: ");
    Serial.println(DHT11.temperature);    
    Serial.println(" C ");
    delay(2000);
}
