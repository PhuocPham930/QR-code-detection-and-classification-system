#include <Servo.h>
#include <string.h>
#define IN1 4
#define IN2 3
#define IN3 6
#define IN4 5
#define CB 2
Servo s1;
Servo s2;
int i = 0;
String data;

void test_dc_run() {
  digitalWrite(IN1, LOW);
  analogWrite(IN2, 250);
}
void test_dc_stop() {
  digitalWrite(IN1, LOW);
  analogWrite(IN2, LOW);
}
void setup() {
  // put your setup code here, to run once:
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(CB, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  s1.attach(9);
  s2.attach(10);
  Serial.begin(9600);
}

void loop() {
  s1.write(180);
  s2.write(0);
    


  int cbState = digitalRead(CB);
  
  if (cbState == 1) {
    test_dc_run();
    
  } else {
    test_dc_stop();
    if (Serial.available() > 0) {
    data = Serial.readStringUntil('\n');
    Serial.print("You sent me: ");
    Serial.println(data);
  }
    delay(3000);
  
    if (data == "do") {
      test_dc_run();
      s1.write(135);
      delay(8000);
      s1.write(180);
      delay(1000);
    } else if (data == "xanh") {
      test_dc_run();
      s2.write(45);
      delay(8000);
      s2.write(0);
      delay(3000);
    }
  }
}
