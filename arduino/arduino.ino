#include <Wire.h>
#include <LiquidCrystal_I2C.h>


// Обращение к кнопкам по именам
#define LEFT 0
#define RIGHT 1
#define UP 2
#define DOWN 3
#define OK 4
#define ESC 5
char names[6][6] = { "LEFT", "RIGHT", "UP", "DOWN", "OK", "ESC" }; // Названия кнопок
int keyboard[6] = { 2, 4, 6, 3, 7, 5 };                            // Номера пинов для кнопок
int kbd_state[6];                                                  // Состояние кнопок (LOW-нажата, HIGH-отпущена)

// Создание объекта LCD
LiquidCrystal_I2C lcd(0x27,20,4);  

void setup() {
// Инициализация COM порта
  Serial.begin(115200);
  Serial.println("welcome");
// Инициализация клавиатуры  
  for (int i = 0; i < 6; i++) {
    pinMode(keyboard[i], INPUT_PULLUP);
    kbd_state[i] = HIGH;
  }
// Инициализация LCD
  lcd.init();
  lcd.backlight();
  //lcd.print("Hello");
  //delay(2000);
}

void loop() {
// Обработка сообщений от Orange Pi Zero
  if (Serial.available()>0){
    char buf[20];
    char *s=buf;
    byte n=Serial.readBytesUntil('\n',buf,20);
    buf[n]='\0';
    char module = s[0];
    s++;
    switch (module){
      case 'l':
        lcdCommand(s);
        break;        
    }         
    Serial.println("OK");          
  }
}

// Функции работы с LCD 
void lcdCommand(char *cmd)
{
  char command = cmd[0];
  char *s= ++cmd;
  /*lcd.print(command);
  lcd.print('>');
  lcd.print(s);
  lcd.print('|');*/  
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
      char sx[3]={s[0],s[1],0}, sy[2]={s[2],0};
      int x = atoi(sx);       
      int y = atoi(sy);
      lcd.setCursor(x,y);
      break;
  }  
}

// Функции работы с клавиатурой




// Обработка нажатия кнопок
void buttonRead(){
  for (int i = 0; i < 6; i++) {
    int state = digitalRead(keyboard[i]);
    if (state == HIGH && kbd_state[i] == LOW) {
      kbd_state[i] = HIGH;
    }
    if (state == LOW && kbd_state[i] == HIGH) {
      delay(50);
      if (digitalRead(keyboard[i]) == LOW) {
        kbd_state[i] = LOW;
      }
    }
  }
}
