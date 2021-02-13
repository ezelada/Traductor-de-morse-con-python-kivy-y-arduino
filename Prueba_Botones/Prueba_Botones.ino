const int BOT1 = 2;
const int BOT2 = 3;
const int BOT3 = 4;
int estado1;
int estado2;
int estado3;
String data = "";

void setup() {
  
  Serial.begin(9600);
  pinMode(BOT1, INPUT);
  pinMode(BOT2, INPUT);
  pinMode(BOT3, INPUT);
  
  }

void loop() {
  estado1 = digitalRead(BOT1);
  estado2 = digitalRead(BOT2);
  estado3 = digitalRead(BOT3);

  if (estado1 == LOW) {
    delay(400);
    if (estado1 == LOW) {
      data += "-";
    }
  }

  if (estado2 == LOW) {
    delay(400);
    if (estado2 == LOW) {
      data += ".";
    }
  }
  
  if (estado3 == LOW) {
    delay(400);
    if (estado3 == LOW) {
      Serial.println(data);
      data = "";
    }
  }
  
}
