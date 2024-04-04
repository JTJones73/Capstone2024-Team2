# Projectile Path Sensor Signoff
## Subsystem Function
The projectile Path sensor subsystem must detect when a projectile is launched and determine which of the 15 possible paths the projectile will take. This is expected to be the first sensor data sent to the interceptor. This data provies the required yaw angle to properly intercept the incoming projectiles.
## Constraints
- Constrain 1: Create an interceptor capable of functioning on its own without outside interaction. 
  - Reasoning: Do to a constumer requirement the interceptor and all external sensor post must be autonomous after intial startup.
- Constraint 2: Design a sensor array that can detect approaching objects and relay their locations to the interceptor.
  - This constraint was developed to meet the requirement to have a sensor that has determines when a projectile has begun to move towards the interceptor. Also, the sensor will determine the path at which the projectile is heading towards to the interceptor.
- Constraint 3: Design a sensor array that operates on battery power.
  - All sensor posts must be powered with a standalone powersupply and must not receive power from a outlet. This originated from a constraint provided by the constumer.
- Constraint 4: The Design shall implement the best remote battery power solution to limit the interceptor’s environmental impact.
  - This constraint addresses the broader impacts of current enviromental impacts of disposing batteries.
- Constaint 5: Design a system that complies with the ANSI Z136.1 Standard
  - This constraint is required due to the use of laser sensors to determine when a projectile is launched. This Standards clasifies lasers as well as defines the required PPE while useing lasers.
- Constraint 6: Use a processing unit that has the capability to support all required sensors as well as ability to connect to a ESP device.
  - It is expected that 30 I/O ports are required to power the laser sensor array. The Microprocessor must be capabile of suppling sufficent power. Also, another port to comunicate and power the ESP device required in the wireless communication subsystem.
## Schematic
## Analysis
### Battery
Due to the constraint of having to use battery power all sensors, lasers, and microcontroller must be ran with a standalone battery power supply. The battery chosen is two Samsung 25R 18650 [2] in series. This results in a 7.2 Volt 2500 mAh battery. This voltage is chosen due to the reccomend voltage of the atmega 2560 being 7-12 Volts[1]. Do to battery voltages decreasing as they discharge, only the mAh before the voltage decreases past 3.5 volts is taken into calculations. According to the Samsumung 25R battery data sheet, the battery discharges 1700 mAh before the voltage reaches below 3.5 volts [3]. In the table below show the total battery consumption on the system. In this table we can conclude that the external battery selected can power the sensor array for roughly 3 hours.

| Device | Current Draw |
| ------ | --------------- | 
| Laser Array | 450 mA at 5 Volts and ~ 322 mA at 7 Volts| 
| Buck Converter| 88% efficency ~39 mA |
| Atmega 2560 | Maximum current 200 mA |
| Total | 561 mA |

## Bill of Materials

| Item | Part Number | Quantity | Price Per Unit | Total Cost |
| ----------------- | ---- | ----| ------| ------ |
| Elegoo Atmega 2560 | EL-CB-002 | 1 | $20.99 | $20.99 | 
| Samsung 25R 18650 | 25R | 2 | $3.75 | $7.50 |
| 18650 Battery Holder | 114090053 | 1 | $1.49 | $1.49 |

## Refrences
[1] AZ Delivery, "Ky-008 Laser Trasmitter Modul Datenblatt"m ky-008, 2017. \
[2] DFRobot, "20W Adjustable DC-DC Buck Converter with Digital Display", DFR0379, Feb, 2017. \
[3] “114090053,” Digikey, https://www.digikey.com/en/products/detail/seeed-technology-co.,-ltd/114090053/10451921?utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_Low%20ROAS%20Categories&utm_term=&utm_content=&utm_id=go_cmp-20243063506_adg-_ad-__dev-c_ext-_prd-10451921_sig-Cj0KCQjwn7mwBhCiARIsAGoxjaL8WD90igyFKSXdHxOkua8whupC5BGHClnKJqEKValV6_VOdacOF8caAilXEALw_wcB&gad_source=1&gclid=Cj0KCQjwn7mwBhCiARIsAGoxjaL8WD90igyFKSXdHxOkua8whupC5BGHClnKJqEKValV6_VOdacOF8caAilXEALw_wcB (accessed Apr. 4, 2024). 
[3] “ELEGOO MEGA R3 Board ATmega 2560 + USB Cable Compatible with Arduino IDE Projects RoHS Compliant,” Amazon.com.
[1] "Mega 2560 Rev3," docs.arduino.cc, Available: https://docs.arduino.cc/hardware/mega-2560/#features. [accessed Apr. 4, 2024]. \
[2] Microchip, "ATmega640/V-1280/V-1281/V-2560/V-2561/V" , Atmega2560, Mar. 2025 [Revised May. 2020]. \
[3] “Samsung 25R 18650 2500mah 20A battery,” 18650BatteryStore.com, https://www.18650batterystore.com/products/samsung-25r-18650? utm_campaign=21017394957&utm_source=x_c&utm_medium=cpc&utm_content=&utm_term=_&adgroupid=&gad_source=4&gclid=Cj0KCQjwn7mwBhCiARIsAGoxjaIDVn2o2IZExphwsLASVktA_GrIyjrilURVrJArgcjTx32l40fdsE0aAlPREALw_wcB [accessed Apr. 4, 2024]. \
[4] Samsung, "Introduction of INR18650-25R", INR18650-25R, OCT. 2013. 