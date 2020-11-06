/*
Blink
Este código faz o led do pino 13 piscar no intervalo de 1 segundo
*/

// variável global, apenas para facilitar a indicação da porta em todo código
const int led = 13;  

void setup() {
     // função que define o pino (qualquer um) e o modo de funcionamento
     pinMode(led, OUTPUT);
}

void loop() {
      // função que grava no pino digital o nível, neste caso o valor de tensão alto
     digitalWrite(led, HIGH);
      // pausa no processamento em 1000 milisegundos
     delay(1000);
     // gravando o nível baixo no pino 13
     digitalWrite(led, LOW);
     delay(1000);
}
