int t = 2;
int e = 3;
int led = 13;
int buzzer = 5;
int pir = 6;
int state = 0;
void setup()
{
pinMode(t, OUTPUT);
pinMode(e, INPUT);
pinMode(led,OUTPUT);
pinMode(pir,INPUT);
Serial.begin(9600);
}

void loop()
{
digitalWrite(t, LOW);
digitalWrite(t, HIGH);
delayMicroseconds(10);
digitalWrite(t, LOW);
float duration = pulseIn(e, HIGH);
float distance = (duration * 0.034) / 2;
Serial.print("Distance :");
Serial.println(distance);

if(distance < 10)
{
digitalWrite(led,HIGH);
delay(1000);
digitalWrite(led,LOW);
delay(1000);
tone(buzzer,450);
delay(1000);
noTone(buzzer);
delay(1000);
}

state = digitalRead(pir);
delay(1000);
if (state == HIGH) {
digitalWrite(led, HIGH);
tone(buzzer,450);
delay(1000);
noTone(buzzer);
delay(1000);
} else {
digitalWrite(led, LOW);
}
double a = analogRead(A0);
double t = (((a/1024)*5)-0.5)*100;
Serial.print("Temperature:");
Serial.println(t);
delay(1000);
}
