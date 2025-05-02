#include <Servo.h>

Servo PD;
Servo CD;
Servo PieI;
Servo CI;

int num=0,numant=0;

void setup()
{
  Serial.begin(9600);
  PD.attach(11);
  CD.attach(9);
  PD.attach(8);
  
}


void loop() {
  if (Serial.available()) {
    String num_str = Serial.readStringUntil('\n'); // Lee la cadena hasta el delimitador '\n'
    num = num_str.toInt(); // Convierte la cadena a un entero
    if(num!=numant){
      numant=num;
      if(num==1){ //plastic
        CI.write(180);
        delay(1000);
        CI.write(90);
        delay(1000);
      }
      if(num==2 or num==6){ //paper and cardboard
        Serial.begin (9600);
    PD.attach(8);
  CD.attach(9);
  DD.attach(11);
  DD.write(90);
  CD.write(90);
  delay(500);
  DD.write(110);
  delay(500);
  DD.write(115);
  delay(500);
  CD.write(170);
  delay(500);
  CD.write(70);
  delay(500);
  CD.write(90);
      }
      if(num==7 or num==3){ //trash
        PieI.write(180);
        delay(1000);
        PieI.write(90);
        delay(1000);
      }
    }

  }
}
