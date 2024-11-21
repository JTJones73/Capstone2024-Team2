# Experimental Analysis

## Introduction 
The purpose of this report is to verify the requirements for the project and explain the procedures used to validate results. The results will be compared against the measures of success outlined in the project proposal to determine if the project was successful. This will also detail what the next steps are moving forward.

### System Critical Constraints

| Item # | Constraint/Specification | Subsystem Affected | 
|-|-|-|
| 1 | Shall Create an interceptor capable of functioning on its own without outside interaction. | All Subsystems |
| 2 | The System shall be capable of sensing all 15 lines when a projectile is released.  | Projectile Path Sensor |
| 3 | All external sensors shall be capable of running on battery power.  | Projectile Path sensor and Velocity and Acceleration Sensor |
| 4 | The interceptor shall have a power system be capable of providing power to each component in the main housing. | Power & Housing | 
| 5 | The interceptor shall have a firing system capable of firing a projectile. | Firing | 
| 6 | The interceptor shall have a firing system capable of stopping the firing motor once a round has been fired. | Firing |
| 7 | The interceptor shall have an external sensor capeable of obtaining a distance measurements and time at multiple points across each path. | Velocity and Acceleration|
| 8 | The interceptor shall move into aiming position based on input gathered from sensor data. | Aiming |
| 9 | The interceptor shall move into aiming position before the projectile moves away from the interceptor's range | Aiming |
| 10 | The interceptor shall be able to detect and locate targets head on. | Head on Sensor |
| 11 | When the interceptor is sensing head on targets the maximum sensing latency shall not exceed 100ms. | Head on Sensor |
| 12 | The interceptor shall be able to wirelessly communicate with the sensor array. | Networking |
| 13 | The interceptor shall be able to wirelessly recieve information from no less than 6 devices at the same time. | Networking |

## Analysis
### Projectile Path Sensor
The system critical constraints that are met by the projectile path sensor are:
1. Shall Create an interceptor capable of functioning on its own without outside interaction.
2. The System shall be capable of sensing all 15 lines when a projectile is released.
3. All external sensors shall be capable of running on battery power.

To verify that these constraints are met by the system, the projectile path sensor will be powered on using a 9V battery and with no external interaction a ball will be dropped from all 15 lines to verify that the system can detect and transmit this information to the interceptor. This test will be ran twice to verify that the system did not have any false posisitives.

| Line Number | Projectile Detected Trial 1|Projectile Detected Trial 2|
|---|---| ---|
| 1 | Yes | Yes |
| 2 | Yes | Yes |
| 3 | Yes | Yes |
| 4 | Yes | Yes |
| 5 | Yes | Yes |
| 6 | Yes | Yes |
| 7 | Yes | Yes |
| 8 | Yes | Yes |
| 9 | Yes | Yes |
| 10 | Yes | Yes |
| 11 | Yes | Yes |
| 12 | Yes | Yes |
| 13 | Yes | Yes | 
| 14 | Yes | Yes |
| 15 | Yes | Yes |

With this test, we can verify all required constraints for the projectile path sensor are met. First, all 15 possible lines can be detected and this data wirelessly transmits to the main interceptor. Also, this test verifies that the entire sensor array is able to be powered. Finally, the entire subsystem is autonomous. With this test, we can conclude that the Projectile Path Sensor is complete and fully functioning.

### Velocity and Acceleration Sensor
The system critical constraints that are met by the Velocity and Acceleration Sensor system are:
1. Shall Create an interceptor capable of functioning on its own without outside interaction.
3. All external sensors are capable of running on battery power.
7. The interceptor shall have an external sensor capable of obtaining a distance measurement and time at multiple points across each path.

To verify that the constraint 7 is met by the system, the Velocity and Acceleration sensor will be set up on the center of the second sensor post like it will be for the competition and is to be tested in that positon. To test that the system is capable of obtaining a distance measurement and time at multiple points on each path and satisfies this constraint the sensor will be aimed at each line and a ball will be placed to verify that a distance measurement and time is able to be recorded at multiple places. Point 1 is 27 inches away from the sensor, point 2 is 25 inches away from the sensor, and point 3 is 23 inches away from the sensor.

Test Results:

With the results from this test shown in the table below it has been confirmed that the system meets critical constraint 7. This data shows that the system was able to successfully detect, measure the distance, and take a timestamp of the golf ball at several points on every line the golfball can travel on. The system meets the base requirements for this constraint but there could be inprovements made on the accuracy and prevention of false detections.

| Line Number | Projectile Detected & Time Recorded Point 1 | Projectile Detected & Time Recorded Point 2 | Projectile Detected & Time Recorded Point 3 |
|---|---|---|---|
| 1  | Yes | Yes | Yes |
| 2  | Yes | Yes | Yes |
| 3  | Yes | Yes | Yes |
| 4  | Yes | Yes | Yes |
| 5  | Yes | Yes | Yes |
| 6  | Yes | Yes | Yes |
| 7  | Yes | Yes | Yes |
| 8  | Yes | Yes | Yes |
| 9  | Yes | Yes | Yes |
| 10 | Yes | Yes | Yes |
| 11 | Yes | Yes | Yes |
| 12 | Yes | Yes | Yes |
| 13 | Yes | Yes | Yes |
| 14 | Yes | Yes | Yes |
| 15 | Yes | Yes | Yes |

[Video][def1]

[def1]: https://youtu.be/kAdy6xZ5rTo

To verify that constraints 1 and 3 are met by the system, the Velocity and Acceleration sensor will be powered by a 3.7V LiPo battery and will be set up and have the same placement as in the previous test. To ensure the system is capable of operating without outside intervention and running on battery power the following test will be conducted. After the sensor is set up as previously described a ball will be dropped on line 1 to verify that the sensor will turn to the line to obtain the distance and time measurements and transmit this information to the interceptor. This will prove that the system is capable of operating without outside interaction and running on battery power.

Expected Results: 

Given that the networking subsystem has been proven to be working in the Projectile Path Sensor, and constraint 7 has been confirmed when the networking is integrated into the velocity and acceleration it is expected that the system will be able to confirmed that the system is autonomous and able to run on batteery power.
### Head on Sensor
10. The interceptor shall be able to detect and locate targets head on.
11. The interceptor must be able to detect the heigh of the target to determine which line the target is being sent on.
To confirm these constraints targets shall be sent one each line to confirm the camera's ability to focus on each target and relay that to the aiming system to accurately determine the path the target is taking to ensure proper interception.

The following demonstration shows the head on sensor in conjunction with the projectile path sensor to determine which path the target is taking. The camera subsystem is determining the height of the incoming target by consdering all predicted locations in the past 500ms before tripping the projectile path sensor.

[Level 2 Video][def1337]

[def1337]: https://youtu.be/fpIcUL79n6I

The next demonstration shows the head on sensor working with the projectile path sensor to confirm the target is on level 1

[Level 1 Video][def1338]

[def1338]: https://youtu.be/74Y7jp9s-U8

This tabulated trial was to confirm the sensor's ability to distinguish adjacent lines. These lines 1 - 15 are on the bottom row while lines 16 - 30 are on the second row.

| Adjacent Line Numbers | Results |
|---|---|
| 1 & 16  | Yes |
| 2 & 17  | Yes |
| 3 & 18  | Yes |
| 4 & 19  | Yes |
| 5 & 20  | Yes |
| 6 & 21  | Yes |
| 7 & 22  | Yes |
| 8 & 23  | Yes |
| 9 & 24  | Yes |
| 10 & 25 | Yes |
| 11 & 26 | Yes |
| 12 & 27 | Yes |
| 13 & 28 | Yes |
| 14 & 29 | Yes |
| 15 & 30 | Yes |

### Networking
12. The interceptor shall be able to wirelessly communicate with the sensor array.
13. The interceptor shall be able to wirelessly recieve information from no less than 3 devices at the same time.

To confirm these constraints an experiment was set up to confirm the networking subsystem could allow the sensor array to wirelessly communicate with the interceptor. From here 4 devices were connected and UDP packets were sent to the server which displays the packet's payload.


[Networking Video][def1339]

[def1339]: https://youtu.be/EngO91Z2Qtg

The following tabulated trial was to confirm that each connected device was able to send a payload and be recieved from the server script.


| Device | Results |
|---|---|
| Head on Position Sensor  | Yes |
| Projectile Path Sensor  | Yes |
| Android Device  | Yes |


### Power & Housing
The critical constraints that are met by the power and housing system are: 

4. The interceptor shall have a power system be capable of providing power to each component in the main housing.

To verify that this constraint is met each electronic device will be powered on the interceptor at the same time. Each component will then be analyzed to verify that it is receiving power. In addition the E-Stop will be tested to ensure that it will turn off the motors when pressed. 

Results: 

Each motor turned when receiving power at the same time as the others. Additionally the buzzer and the lighting in the housing remained on. Finally the Raspberry Pi and the Arduino continued to receive power. The E-Stop functioned correctly by disabling the motors when pressed. 

The test above and the results found ensure that the Power & Housing system functions as intended and without error. By powering each motor at the same time the maximum power from the interceptor was placed on the PSU at once. The result has shown that the power system can handle the load well. In addition the E-Stop is shown to effectively prevent power from flowing to the motors. This shows that the E-Stop functions as intended. 

### Aiming
The system critical constraints that are met by the aiming system are:
1. Shall Create an interceptor capable of functioning on its own without outside interaction.
8. The interceptor shall move into aiming position based on input gathered from sensor data.
9. The interceptor shall move into aiming position before the projectile moves away from the interceptor's range

To verify that these constraints are met by the system, the main aiming control unit will be powered and recieve data from the raspberry pi usb port and with no external interaction. To simulate position data being sent, the user will input the position data manually and show where the aiming system moves based on that input. This then will be timed based on the greatest number of steps that the aiming motors took to move into position and calulate the aiming duration based on the step speed of the motors. 
### Firing

The system critical constraints that are met by the firing system are:
1. Shall Create an interceptor capable of functioning on its own without outside interaction.
5. The interceptor shall have a firing system capable of firing a projectile.
6. The interceptor shall have a firing system capable of stopping the firing motor once a round has been fired.


To verify that these constraints are met by the system, the firing motor will be powered on using the housings 12-volt power supply. The main code will then be used to verify that when a signal is sent from the aiming subsystem, the motor turns on, releasing a single round, and will be powered off once the proximity sensor is in line with the timing piece. 

Results: 
https://youtube.com/shorts/PYR-_0FZ6-E?feature=share

When the test signal was sent the motor activated autonomously and stopped when the timing piece was in line with the prox sensor. Furhter testing and tuning (such as moving the timing piece slightly) may need to be done to ensure the design works properly once we are able to have the load from the remaining pieces from the firing mechanism mounted to the rest of the design, hence changing the load put upon the motor once the ME team has completed that piece. 
