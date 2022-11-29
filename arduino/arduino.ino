
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display
boolean command=false;

void setup()
{
  Serial.begin(9600);
  while (!Serial){}

  lcd.init();                       
  lcd.backlight();
}

void cmd_wrt(String s){
  int x = s.substring(0,1).toInt();
  int y = s.substring(1,2).toInt();  
  
  lcd.setCursor(x,y);
  String msg = s.substring(2);
  lcd.println(msg);    
}

void loop()
{
  if (Serial.available()>0){
    String s = Serial.readString();
    s.trim();
    char command = s.charAt(0);
    s = s.substring(1);
    switch (command)  {
      case 'w':
        cmd_wrt(s);
        break;
      case 'f':
        lcd.noBacklight();
        break;
      case 'n':
        lcd.backlight();
        break;                
    }          
    s = s + "  " + s;
    Serial.println(s);                   
  }
}
