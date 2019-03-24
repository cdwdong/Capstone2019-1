#include <LiquidCrystal_I2C.h>

#include <LiquidCrystal.h> 
//#include <Wire.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

byte addrs[] = {0x27, 0x3F};
byte addr = 0;
int error;
int Meansuring_Times = 50;

//이곳의 ADDR 은 중요하지 않습니다.
//LiquidCrystal_I2C lcd(0x00, 16, 2);

int Vo = A0; 
int V_LED = 8;     

float Vo_value = 0;
float Voltage = 0;
float dustDensity = 0;
float dustCleanVoltage = 0.62;
 
int samplingTime = 280;
int deltaTime = 40;
int sleepTime = 9680;

void setup()
{
  //LCD_Setup();
  lcd.begin(16, 2);
   // Print a message to the LCD.
  //lcd.print("dust");
  
  Serial.begin(9600);

  /*digital output:*/
  pinMode(V_LED, OUTPUT);

 /*analog input:*/
  pinMode(Vo, INPUT);

  lcd.clear();
  lcd.print("Booting......");
}

/** references : 
 * http://blog.naver.com/PostView.nhn?blogId=darknisia&logNo=221222455928
 * http://arduinodev.woofex.net/2012/12/01/standalone-sharp-dust-sensor/
 * */
 // 미세먼지 센서(GP2Y1010AU0F)
 // : 적외선 발광 다이오드(IRED)와 포토다이오드가 대각선으로 배치되어 공기 중 먼지의 반사광을 감지 
void loop()
{
 
  Computing_Mean(); 
  PrintSerial();
  PrintLCD();
  
  delay(500);
}
/*
void LCD_Setup()
{
  Wire.begin();
  Serial.begin(9600);
  for (int i = 0; i < sizeof(addrs) ; i++) 
  {
    Wire.beginTransmission(addrs[i]);
    error = Wire.endTransmission();
    if (error == 0) {
      addr = addrs[i];
      break;
    }
  }
  while (addr == 0) 
  {
    Serial.println("lcd not connected");
    delay(1000);
  }
  lcd = LiquidCrystal_I2C(addr, 16, 2);
  Serial.println("check finished");
  Serial.println(addr, HEX);
  lcd.begin();
  lcd.backlight();
  lcd.clear();
  lcd.print("Hello, world!");
  lcd.setCursor(0, 1);
  lcd.print("ADDR : ");
  lcd.print(addr, HEX);

}
*/
void Computing_Mean()
{
  float mean = 0;
  float meanV = 0;
  
  Voltage = 0;
  dustDensity = 0;
  
  for(int i = 0; i < Meansuring_Times; i ++)
  {
    Voltage = 0;
    dustDensity = 0;
    Computing_dust();
    mean = mean + dustDensity;
    meanV = meanV + Voltage;

    delay(100);
  }

  mean = mean / Meansuring_Times;
  meanV = meanV / Meansuring_Times;

  dustDensity = mean;
  Voltage = meanV;
}
void Computing_dust()
{
  Vo_value = 0;
  Voltage = 0;
  
  digitalWrite(V_LED,LOW);  //ired 'on'
  delayMicroseconds(samplingTime);
  Vo_value = analogRead(Vo); //read the dust value
  delayMicroseconds(deltaTime);// pulse width 0.32 - 0.28 = 0.04 msec
                               //0.32 msec의 펄스폭을 유지하기 위해 필요한 코드입니다

  digitalWrite(V_LED,HIGH); //ired 'off'
  delayMicroseconds(sleepTime);


/*
이 센서의 출력전압(Vo)는 먼지가 없을 때의 출력전압(Voc)과 먼지 농도(ΔV)에 비례하여 출력됩니다. 
다시 표현하면 ΔV = Vo – Voc
미세먼지 농도[µg/m³] = (Vo – Voc) / 0.005
*/
  Voltage = Vo_value * (5.0 / 1024.0);

  dustDensity = (Voltage - dustCleanVoltage)/0.005;
}

void PrintSerial()
{
  Serial.print(" Raw Signal Value (0-1023):");
  Serial.print(Vo_value);
  Serial.print(" | Volatage:");
  Serial.print(Voltage);
  Serial.print(" | Dust Density:");
  Serial.print(dustDensity);
  Serial.print("[ug/m3]");
  Serial.println();
  Serial.println();
  Serial.println();
}

void PrintLCD()
{
  lcd.clear();                                     // lcd의 화면을 지웁니다.
  lcd.setCursor(0, 0);                            
  lcd.print("Jimin's PM2.5");           
  lcd.setCursor(0, 1);                            
  lcd.print(Voltage);
  lcd.print("V ");
  lcd.print(dustDensity);         
  lcd.print("ug/m3"); 
}

