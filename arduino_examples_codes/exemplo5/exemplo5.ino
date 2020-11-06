#include <SPI.h>
#include <Ethernet.h>

uint32_t timer = 0;

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192,168,1,2);          
IPAddress gateway(192,168,1,1);	     
IPAddress subnet(255, 255, 255, 0);  
 
EthernetServer server(80);
 
void setup()
{
  Ethernet.begin(mac, ip, gateway, subnet);
  server.begin();
}
 
void loop() {
 
  EthernetClient client = server.available();

  if (client) 
  {

    boolean currentLineIsBlank = true;

    while (client.connected()) 
    {
      if (client.available()) 
      {
        char c = client.read();
        Serial.write(c);

        if (c == 'n' && currentLineIsBlank) 
        {
          
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");
          client.println("Refresh: 2"); //Recarrega a pagina a cada 2seg
          client.println();

          client.println("<!DOCTYPE HTML>");
          client.println("<html>");

           
          client.print("<H1>ARDUINO ONLINE</H1>");
                   
          client.println("</html>");
          break;
        }
        if (c == 'n') {
          currentLineIsBlank = true;
        } 
        else if (c != 'r') {
          currentLineIsBlank = false;
        }
      }
    }

    delay(1);

    client.stop();
    }
}
