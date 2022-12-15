#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#include <OneWire.h>
#include <DallasTemperature.h>

// Константы для датчиков уровня
#define LEVELS_COUNT  4
#define AKKUMULATOR_L 0
#define HIGH_L        1
#define LOW_L         2
#define ALARM_L       3

// Константы для 1-WARE
#define ONE_WIRE_BUS 8

// Константы для клавиатуры
#define LEFT 0
#define RIGHT 1
#define UP 2
#define DOWN 3
#define OK 4
#define ESC 5

// Переменные для задержки
unsigned long last=0;
int is_wait = -1;
int slp = 0;

//Переменные для датчиков уровня
int levels[4] = { 9, 10, 11, 12 };
int level_state[4];

// Переменные для 1-Wire

// Переменные для клавиатуры
int keyboard[6] = { 2, 4, 6, 3, 7, 5 };                            
int kbd_state[6];                                                  
char kbd_buf[10];
char kbd_pointer=-1;

// Создание объекта LCD
LiquidCrystal_I2C lcd(0x27,20,4);  

// Создание объекта DS18B20
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensor(&oneWire);
DeviceAddress Thermometer;

void setup() {
  // Инициализация COM порта
  Serial.begin(115200);
  Serial.println("welcome");
  // Инициализация датчиков уровня
  for (int i = 0; i<LEVELS_COUNT; i++){
    pinMode(levels[i], INPUT);        
  }
  // Инициализация клавиатуры  
  for (int i = 0; i < 6; i++) {
    pinMode(keyboard[i], INPUT_PULLUP);
    kbd_state[i] = HIGH;
  }
  // Инициализация LCD
  lcd.init();
  lcd.backlight();
  // Инициализация шины 1-Ware
  sensor.begin(); 
}

void loop() {
  // Реализация задерки в миллисекундах
  if (is_wait == 0){
    if (abs( millis()-last ) > slp){
      is_wait = -1;
      Serial.println("OK");      
    }
  }
  readKeyboard();  
  readSerial();
}

// Обработка датчиков уровня
char* readLevels(char s[5]){
  for (int i=0;i<LEVELS_COUNT;i++){
    if (digitalRead(levels[i]) == HIGH)
      s[i]='#';
    else 
      s[i]='_';          
  }  
  s[4]='\0';
  return s;
}

// Обработка датчиков 1 Ware
char* read1Wire(char s[10]){
  for (int i=0; i<10; i++) s[i]=0;
  sensor.requestTemperatures(); 
  float temp=sensor.getTempCByIndex(0);
  dtostrf(temp, 7, 1, s); 
  return s;
}

// Обработка нажатия кнопок
// Используется кольцевой буфер на 8 символов
void readKeyboard(){
  for (int i = 0; i < 6; i++) {
    int state = digitalRead(keyboard[i]);
    if (state == HIGH && kbd_state[i] == LOW) {
      kbd_state[i] = HIGH;
    }
    if (state == LOW && kbd_state[i] == HIGH) {
      delay(50);
      if (digitalRead(keyboard[i]) == LOW) {
        kbd_state[i] = LOW;
        kbd_pointer++;
        kbd_buf[kbd_pointer]=i;
        if (kbd_pointer>9){
          for (int i=0;i<9;i++){
            kbd_buf[i]=kbd_buf[i+1];            
          }
          kbd_pointer--;
        }                        
      }
    }
  }
}

// Обработка сообщений от Orange Pi Zero
void readSerial(){
  if (Serial.available()>0){
    char buf[20];
    char *s=buf;
    byte n=Serial.readBytesUntil('\n',buf,20);
    buf[n]='\0';
    char module = s[0];
    s++;
    char buffer[10];
    switch (module){
      // Вывод на LCD
      case 'l':
        lcdCommand(s);
        Serial.println("OK");
        break;        
      // Чтение нажатых клавиш
      case 'k':
        kbdCommand(s);
        break;
      // Работа с 1-Wire
      case '1':
        Serial.println(read1Wire(buffer));
        break;              
      // Чтение датчиков уровня
      case '2':
        Serial.println(readLevels(buffer));
        break;
      // Задержка на n миллисекунд
      case '3':
        int ms = atoi(s);
        slp = ms;
        is_wait=0;
        last = millis();        
        break;
    }         
  }
}

// Функции работы с клавиатурой
// Возвращает строку 'AB\n', A-код кнопки, B-кол-во оставшихся нажатий.
// Если нажатий нет, возвращает '-1'
void kbdCommand(char *cmd){
  char command = cmd[0];
  char *s= ++cmd;
  char res[5] = "-1\n";
  switch (command){
    case 'r':
      if (kbd_pointer>-1){
        char sa[3];
        itoa(kbd_buf[kbd_pointer], sa, 10);
        res[0]=sa[0];
        kbd_pointer--;
        itoa(kbd_pointer+1, sa, 10);
        res[1]=sa[0];
        res[2]='\n';
      }
      break;  
  }      
  Serial.print(res);
}

// Функции работы с LCD 
void lcdCommand(char *cmd)
{
  char command = cmd[0];
  char *s= ++cmd;
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
