
// #include <Wire.h>
// #include <LiquidCrystal_I2C.h>



#define LEFT 0
#define RIGHT 1
#define UP 2
#define DOWN 3
#define OK 4
#define ESC 5
char names[6][6] = { "LEFT", "RIGHT", "UP", "DOWN", "OK", "ESC" };
int keyboard[6] = { 2, 4, 6, 3, 7, 5 };
int kbd_state[6];
// LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

void setup() {
  Serial.begin(115200);
  Serial.println("welcome");
  for (int i = 0; i < 6; i++) {
    pinMode(keyboard[i], INPUT_PULLUP);
    kbd_state[i] = HIGH;
  }
  // lcd.init();
  // lcd.backlight();
}

void loop() {
  for (int i = 0; i < 6; i++) {
    int state = digitalRead(keyboard[i]);
    if (state == HIGH && kbd_state[i] == LOW) {
      kbd_state[i] = HIGH;
      String s = "Pin " + String(names[i]);
      Serial.println(s + " unpressed.");
    }
    if (state == LOW && kbd_state[i] == HIGH) {
      //kbd_state[i]=state;
      delay(50);
      if (digitalRead(keyboard[i]) == LOW) {
        kbd_state[i] = LOW;
        String s = "Pin " + String(names[i]);
        Serial.println(s + " pressed.");
      }
    }
  }


  /*  if (Serial.available()>0){
    String s = Serial.readString();
    s.trim();
    char module = s.charAt(0);
    s = s.substring(1);
    switch (module){
      case 'l':
        lcdCommand(s);
        break;        
    }         
    Serial.println("OK");          
  }
*/
}


/*
// Функции работы с LCD 
void lcdCommand(String cmd)
{
  char command = cmd.charAt(0);
  String s = cmd.substring(1);
  switch (command)  {
    // Вывод строки
    case 'a':
      lcd.print(s);
      break;
    // Выкл подсветку
    case 'b':
      lcd.noBacklight();
      break;
    // Вкл подсветку
    case 'c':
      lcd.backlight();
      break;                
    // Вкл мигание символа
    case 'd':
      lcd.blink_on();
      break;
    // Выкл мигание символа
    case 'e':
      lcd.blink_off();
      break;      
    //Очистить экран
    case 'f':
      lcd.clear();
      break;                  
    //Включить курсор
    case 'g':
      lcd.cursor_on();
      break;    
    //Выключить курсор
    case 'h':
      lcd.cursor_off();
      break;  
    // Переместить курсор
    case 'i':
      int x = s.substring(0,2).toInt();       
      int y = s.substring(2).toInt();
      lcd.setCursor(x,y);
      break;
  }  
}
*/
