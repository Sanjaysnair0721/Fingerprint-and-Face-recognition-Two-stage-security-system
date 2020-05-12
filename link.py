import RPI.GPIO as GPIO

GPIO.SETMODE(GPIO.BCM)
GPIO.SETUP(15, GPIO.IN)
GPIO.SETUP(14, GPIO.IN)
a="Sanjay S Nair"
b="Elvis Presley"
if GPIO.input(14):
    print("Finger detected - Sanjay S Nair");
    print("Proceed to face verification");
    face_recognition(a,b);
elif GPIO.input(15):
    print("Finger detected - Your Name");
    print("Proceed to face verification");
    face_recognition(a,b);
else
    print("Finger not found");
    
