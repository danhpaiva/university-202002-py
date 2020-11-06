/*
Blink
Este c�digo faz o led do pino 13 piscar no intervalo de 1 segundo
*/

// vari�vel global, apenas para facilitar a indica��o da porta em todo c�digo
const int led = 13;  

void setup() {
     // fun��o que define o pino (qualquer um) e o modo de funcionamento
     pinMode(led, OUTPUT);
}

void loop() {
      // fun��o que grava no pino digital o n�vel, neste caso o valor de tens�o alto
     digitalWrite(led, HIGH);
      // pausa no processamento em 1000 milisegundos
     delay(1000);
     // gravando o n�vel baixo no pino 13
     digitalWrite(led, LOW);
     delay(1000);
}
