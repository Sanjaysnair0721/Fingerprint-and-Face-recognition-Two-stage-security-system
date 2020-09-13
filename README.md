# Two-Stage-security-system
A simple two stage authentication system 
# Contents
- Description
- Components
- Software
- Implementation
# Description
The project is similiar to the multi stage verification tech used in big companies, government for security. It consists of a fingerprint scanning, followed by a face recognition system to provide double security. The face recognition is initiated only if the finger print scan scores a match in its database. Once a match is hit, face recognition is enabled. If both the stages gets a match, access is granted. We will be dealing with the 2 stages here.
https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php
# Components
- Raspberry Pi-
Raspberry Pi 3B is used here. The project can also be done using 3B+ 
- Arduino Uno
- R307 Fingerprint Sensor-
Optical fingerprint sensor with USB1.1/UART interface and TTL logic.
Voltage Level: 4.5 to 6V
- VGA Camera module- 
USB type connector
- Raspberry Pi display- 800 x 440 RGB LCD display
# Software
- Python 3.7.2
- Arduino IDE
- OpenCV
# Implementation
- Connections

For connecting R307 to the Arduino, connect the Vcc and ground accordingly. Then, connect Tx of R307 to Rx of Arduino and Rx of R307 to Tx of Arduino.

For connecting Arduino to Pi, use the   USB2.0 cable. Also, make 2 jumper wire connections between the Pi and Arduino(14 and 15 in Pi, 6 and 7 in Arduino) 
- Code

The fingerfinal.ino program is run in Arduino. When a finger is detected by the fingerprint sensor, it sends a confirmation signal to the Arduino board with a particular confidence value. This signal is accepted bythe code link.py .Once a finger is detected, and then the face_recognition.py program is run to detect the face of the person.Both face_recognition.py and link.py are stored inside Pi. The output will be displayed in the Pi display.

All codes are witte for 2 people ie. my face and fingerprint will be recognised. Replace all "Your Name" phrases with your name in the code. Inside the 'training-data' folder, load 10 of your different images and save it in a folder 's2'. Also, store one image  inside 'test-data' folder as 'test1'. 
