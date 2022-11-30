
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display
boolean command=false;

void setup()
{
  Serial.begin(115200);
  Serial.println("welcome");  
  lcd.init();                       
  lcd.backlight();
}

void loop()
{
  if (Serial.available()>0){
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
}

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


